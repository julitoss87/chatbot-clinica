from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from responses import get_response
import os
from datetime import datetime
import gspread

app = Flask(__name__)

# Ruta temporal
SERVICE_ACCOUNT_FILE = 'google_creds_temp.json'

# Guardar contenido del .json desde variable de entorno
creds_json = os.getenv('GOOGLE_CREDS_JSON')

if creds_json:
    with open(SERVICE_ACCOUNT_FILE, 'w') as f:
        f.write(creds_json)

    try:
        gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
        sheet = gc.open("Conversaciones Whatsapp").sheet1
        print("[INFO] Acceso a Google Sheets exitoso.")
    except Exception as e:
        print(f"[ERROR] No se pudo abrir la hoja: {e}")
        sheet = None
else:
    sheet = None
    print("[ERROR] GOOGLE_CREDS_JSON no está configurada correctamente")

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    phone_number = request.values.get('From', '')
    print("[INFO] Mensaje recibido:", incoming_msg)

    respuesta = get_response(incoming_msg)
    print("[INFO] Respuesta generada:", respuesta)

    # Guardar conversación
    if sheet:
        try:
            sheet.append_row([
                phone_number,
                incoming_msg,
                respuesta,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ])
            print("[INFO] Conversación guardada en Google Sheets.")
        except Exception as e:
            print("[ERROR] No se pudo guardar en Google Sheets:", e)

    # Respuesta a Twilio
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(respuesta)
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)