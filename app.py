from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from responses import get_response

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    print("[INFO] Mensaje recibido:", incoming_msg)

    respuesta = get_response(incoming_msg)
    print("[INFO] Respuesta generada:", respuesta)

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(respuesta)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)