from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from responses import get_response
import os
import csv
from datetime import datetime

app = Flask(__name__)

def guardar_conversacion(numero, mensaje_usuario, respuesta_bot):
    archivo = "conversaciones.csv"
    campos = ["numero", "mensaje_usuario", "respuesta_bot", "fecha_hora"]

    nueva_fila = [numero, mensaje_usuario, respuesta_bot, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]

    archivo_existe = os.path.isfile(archivo)

    with open(archivo, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not archivo_existe:
            writer.writerow(campos)
        writer.writerow(nueva_fila)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    numero = request.values.get('From', '').replace("whatsapp:", "").strip()

    print("[INFO] Mensaje recibido:", incoming_msg)

    respuesta = get_response(incoming_msg)
    print("[INFO] Respuesta generada:", respuesta)

    # Guardar la conversación
    guardar_conversacion(numero, incoming_msg, respuesta)

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(respuesta)

    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)