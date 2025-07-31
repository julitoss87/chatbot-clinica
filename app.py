from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from responses import get_response
import os
import csv
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = Flask(__name__)

# Ruta temporal
SERVICE_ACCOUNT_FILE = 'google_creds_temp.json'

# Guardar contenido del .json desde variable de entorno
creds_json = os.getenv('GOOGLE_CREDS_JSON')

if creds_json:
    with open(SERVICE_ACCOUNT_FILE, 'w') as f:
        f.write(creds_json)

    gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    sheet = gc.open("Conversaciones Whatsapp").sheet1  # Asegúrate de haber creado una hoja llamada "Conversaciones"
else:
    sheet = None
    print("[ERROR] GOOGLE_CREDS_JSON no está configurada correctamente")

# Inicializar Google Sheets solo una vez
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Reemplaza por el ID de tu hoja de cálculo
SPREADSHEET_ID = "1FalJcUSUWiqLkP_bVratzoz6gYcR1wLsFqiqMuFcr_E"
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    phone_number = request.values.get('From', '')
    print("[INFO] Mensaje recibido:", incoming_msg)

    respuesta = get_response(incoming_msg)
    print("[INFO] Respuesta generada:", respuesta)

    # Guardar conversación en Google Sheets si la hoja está disponible
    if sheet:
        try:
            sheet.append_row([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                phone_number,
                incoming_msg,
                respuesta
            ])
            print("[INFO] Conversación guardada en Google Sheets.")
        except Exception as e:
            print("[ERROR] No se pudo guardar en Google Sheets:", e)

    # Responder al usuario
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(respuesta)

    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)