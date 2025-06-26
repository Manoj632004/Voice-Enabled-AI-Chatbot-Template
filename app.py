from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)

BLAND_API_KEY = "YOUR_API_KEY"
PATHWAY_ID = "YOUR_PATHWAY_ID"
START_NODE_ID = "YOUR_START_NODE_ID"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    headers = {
        "Authorization": f"Bearer {BLAND_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "pathway_id": PATHWAY_ID,
        "start_node_id": START_NODE_ID
    }
    response = requests.post("https://us.api.bland.ai/v1/pathway/chat/create", json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        data = data.get("data")
        chat_id = data.get("chat_id")
        return jsonify({"message": "Chat session started", "chat_id": chat_id}), 200
    else:
        return jsonify({"error": "Failed to start chat", "details": response.text}), 500

        
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get("message")
    chat_id = data.get("chat_id")
    if not message or not chat_id:
        return jsonify({"error": "Missing message or chat_id"}), 400
    
    headers = {
        "Authorization": f"Bearer {BLAND_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": message
    }
    response = requests.post(f"https://api.bland.ai/v1/pathway/chat/{chat_id}", json=payload, headers=headers)
    if response.status_code == 200:
        reply = response.json().get("data")
        reply = reply.get("assistant_responses")
        return jsonify({"reply": reply[0]}), 200
    else:
        return jsonify({"error": "Chat message failed", "details": response.text}), 500


@app.route('/stop', methods=['POST'])
def stop():
    return jsonify({"message": "Stop function triggered"})

if __name__ == '__main__':
    app.run(debug=True)
