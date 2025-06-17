from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)

BLAND_API_KEY = "org_0de3d7712bc8fd1d901cf963d9ceb441cc302e41aafac0d8bfbae2800737e911cf5398dc6c6d2c5ac7d169"
PATHWAY_ID = "43daae1b-3cd9-4ba9-8726-a01cd8079cb4"
BLAND_API_URL = "https://us.api.bland.ai/v1/pathway/chat/36b0bbd5-5efa-43a3-82a6-07a07a19f74e"
#chatid = 36b0bbd5-5efa-43a3-82a6-07a07a19f74e
START_NODE_ID = "0e82b9e0-be7a-4acf-88f6-9db6312b401a"
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
