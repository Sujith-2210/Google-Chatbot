from flask import Flask, render_template, request, jsonify, session
import requests
import json
import base64
from io import BytesIO
from PIL import Image
import os
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this to a secure secret key

@app.route('/')
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        api_key = data.get('api_key', '').strip()
        image_data = data.get('image')

        if not api_key:
            return jsonify({'error': 'API key is required'}), 400

        if not message and not image_data:
            return jsonify({'error': 'Message cannot be empty'}), 400

        if 'chat_history' not in session:
            session['chat_history'] = []

        headers = {
            'Content-Type': 'application/json',
            'x-goog-api-key': api_key,
        }

        parts = []
        model = 'gemini-2.5-flash' # Default model for text

        if image_data:
            model = 'gemini-2.5-pro' # Model for images
            prompt = message if message else "extract the details from the image and answer about the image."
            parts.append({"text": prompt})

            # The image data is a base64 string with a prefix, e.g., "data:image/jpeg;base64,"
            # We need to remove the prefix before decoding.
            image_content = image_data.split(',')[1]

            parts.append({
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": image_content
                }
            })
        else:
            parts.append({"text": message})

        gemini_data = {
            "contents": [
                {
                    "parts": parts
                }
            ]
        }

        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
            headers=headers,
            data=json.dumps(gemini_data)
        )

        response.raise_for_status()
        response_json = response.json()

        if 'candidates' in response_json and response_json['candidates']:
            bot_response = response_json['candidates'][0]['content']['parts'][0]['text']

            user_message_to_store = message if message else ("Uploaded an image" if image_data else "")

            session['chat_history'].append({
                'id': str(uuid.uuid4()),
                'type': 'user',
                'message': user_message_to_store,
                'image': image_data, # Store the base64 image data
                'timestamp': None
            })
            session['chat_history'].append({
                'id': str(uuid.uuid4()),
                'type': 'bot',
                'message': bot_response,
                'timestamp': None
            })

            if len(session['chat_history']) > 50:
                session['chat_history'] = session['chat_history'][-50:]
            
            session.modified = True

            return jsonify({
                'success': True,
                'response': bot_response
            })
        else:
            return jsonify({'error': 'No response from Gemini API'}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API request failed: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['chat_history'] = []
    session.modified = True
    return jsonify({'success': True})

@app.route('/get_history')
def get_history():
    history = session.get('chat_history', [])
    return jsonify({'history': history})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
