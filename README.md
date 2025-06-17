# Voice-Enabled-AI-Chatbot-Template
A reusable Flask template that integrates Bland AI’s conversational pathways with voice-based interaction in the browser. Transcribes user speech, sends it to Bland AI, and speaks the AI's response back

## 🚀 How It Works

1. User clicks "Start".
2. Browser captures microphone input.
3. Speech is transcribed and sent to Flask backend.
4. Flask forwards it to Bland AI (`/v1/pathway/chat/{chat_id}`).
5. Response is spoken back to the user in a female voice.
6. Loop continues until stopped.

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/voice-chatbot-bland-flask.git
cd voice-chatbot-bland-flask
```

### 2. Install dependencies
```bash
pip install flask requests
```
### 3. Set your API key
```bash
BLAND_API_KEY = "your_bland_ai_api_key"
```

### 4. Run the Flask server
```bash
python app.py
```

## ✨ Features

- 🔁 Real-time voice interaction
- 🧠 Connects to Bland AI chat pathways
- 🗨️ Speaks responses back using browser’s Text-to-Speech
- 🧩 Modular Flask backend
- 🌐 Simple and clean HTML front-end
