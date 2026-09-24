from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) 

TELEGRAM_TOKEN = '8814109704:AAHS6ZbQPuTjovvqG77ENvi4uWU0Pul9jOw'
CHAT_ID = '527646159' 

@app.route('/api/vota', methods=['POST'])
def vota():
    dati = request.json
    nome = dati.get('nome', 'Sconosciuto')
    presenza = dati.get('presenza', 'Nessuna risposta')
    
    messaggio = (
        f"📩 <b>Nuova risposta per i 21 anni!</b>\n\n"
        f"👤 <b>Invitato:</b> {nome}\n"
        f"🍾 <b>Presenza:</b> {presenza}"
    )
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": messaggio,
        "parse_mode": "HTML"
    }
    
    requests.post(url, json=payload)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)