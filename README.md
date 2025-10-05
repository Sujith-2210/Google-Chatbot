# Gemini AI Chatbot - Flask Web Application

A modern, interactive web-based chatbot powered by Google's Gemini AI with support for text and image conversations.

## Features

- 🤖 **AI-Powered Chat**: Interact with Google's Gemini AI models
- 🖼️ **Image Analysis**: Upload and analyze images with AI
- 💬 **Real-time Chat**: Smooth, responsive chat interface
- 📱 **Responsive Design**: Works perfectly on desktop and mobile
- 🔐 **Secure API Key Storage**: Client-side API key management
- 📝 **Chat History**: Persistent chat history during session
- 🎨 **Modern UI/UX**: Beautiful gradient design with animations

## Installation

### Prerequisites
- Python 3.7 or higher
- Google Gemini API key ([Get one here](https://ai.google.dev/))

### Setup Steps

1. **Clone or download the project files**
   ```bash
   mkdir gemini-chatbot-flask
   cd gemini-chatbot-flask
   ```

2. **Create the project structure**
   ```
   gemini-chatbot-flask/
   ├── app.py
   ├── requirements.txt
   ├── templates/
   │   └── index.html
   └── static/
       └── uploads/
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create necessary directories**
   ```bash
   mkdir -p templates static/uploads
   ```

5. **Add the files**
   - Copy `app.py` to the root directory
   - Copy `index.html` to the `templates/` directory
   - Make sure `static/uploads/` directory exists for image uploads

## Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Configure API Key**
   - Click the "API Key" button in the header
   - Enter your Google Gemini API key
   - Click "Save"

## Usage

### Text Conversations
- Type your message in the input field
- Press Enter or click the send button
- Wait for the AI response

### Image Analysis
- Click the image upload button (📷)
- Select an image file (PNG, JPG, JPEG)
- Optionally add a text prompt
- The AI will analyze and describe the image

### Managing Chat
- **Clear History**: Click the "Clear" button to reset the conversation
- **API Configuration**: Click "API Key" to update your API key

## Configuration

### Environment Variables (Optional)
You can set these environment variables instead of using the UI:

```bash
export GEMINI_API_KEY="your-api-key-here"
export FLASK_ENV="development"  # For development
export FLASK_ENV="production"   # For production
```

### Security
- Change the `secret_key` in `app.py` to a secure random string
- For production, use environment variables for sensitive data
- Consider implementing rate limiting for production use

## API Endpoints

- `GET /` - Main chat interface
- `POST /chat` - Send text message to AI
- `POST /upload` - Upload image with optional text
- `POST /clear_history` - Clear chat history
- `GET /get_history` - Retrieve chat history

## Troubleshooting

### Common Issues

1. **"API key is required" error**
   - Make sure you've entered a valid Gemini API key
   - Check if the API key has the necessary permissions

2. **Image upload fails**
   - Ensure image is under 5MB
   - Use supported formats: PNG, JPG, JPEG
   - Check internet connection

3. **Server won't start**
   - Make sure all dependencies are installed
   - Check if port 5000 is available
   - Verify Python version (3.7+)

### Error Messages
- **"No response from Gemini API"**: API might be down or key invalid
- **"Network error"**: Check your internet connection
- **"Invalid file type"**: Use PNG, JPG, or JPEG images only

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set `debug=False` in app.py
2. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

### Docker (Optional)
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## Customization

### Styling
- Edit the CSS in `templates/index.html` to change colors and layout
- Modify the gradient backgrounds and animations
- Adjust responsive breakpoints for mobile

### Features
- Add user authentication
- Implement conversation export
- Add more AI model options
- Include conversation search

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review the Google Gemini API documentation
3. Open an issue on the project repository

---

**Note**: This application requires a valid Google Gemini API key to function. The API key is stored locally in your browser and never sent to any external servers except Google's Gemini API.