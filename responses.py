user_states = {}

def get_response(user_input, user_id="default"):
    user_input = user_input.lower().strip()
    
    if user_id not in user_states:
        user_states[user_id] = "main_menu"

    state = user_states[user_id]

    # MENÚ PRINCIPAL
    if state == "main_menu":
        if user_input in ["1", "cirugías faciales"]:
            user_states[user_id] = "facial_menu"
            return (
                "👃 CIRUGÍAS FACIALES:\n"
                "1. Rinoplastia\n"
                "2. Blefaroplastia (párpados)\n"
                "3. Lifting facial\n"
                "4. Bichectomía\n"
                "Escribe el número o 'volver' para regresar al menú principal."
            )
        elif user_input in ["2", "cirugías corporales"]:
            user_states[user_id] = "corporal_menu"
            return (
                "💪 CIRUGÍAS CORPORALES:\n"
                "1. Liposucción\n"
                "2. Abdominoplastia\n"
                "3. Aumento de glúteos\n"
                "4. Lipoescultura\n"
                "Escribe el número o 'volver' para regresar al menú principal."
            )
        elif user_input in ["3", "agendar", "agenda una cita"]:
            return "🗓️ Para agendar una cita, por favor indícanos tu nombre completo y un número de contacto. Un asesor te escribirá en breve."
        elif user_input in ["4", "promociones"]:
            return "🔥 Nuestras promociones actuales:\n- 15% de descuento en rinoplastia\n- Combo lipo + abdominoplastia\n- Consulta gratuita en julio"
        elif user_input in ["5", "ubicacion", "ubicación"]:
            return "📍 Nos encontramos en Bogotá, Cra 15 #123-45. Atendemos de lunes a sábado de 8:00 am a 6:00 pm."
        elif user_input in ["6", "asesor", "hablar con asesor"]:
            return "👩‍⚕️ Un asesor se comunicará contigo en unos minutos. También puedes escribir directamente a nuestro WhatsApp empresarial."
        else:
            return (
                "👋 Bienvenido(a) a Clínica Guadalupe ✨\n"
                "Escribe el número de la opción que deseas:\n"
                "1. Información sobre cirugías faciales\n"
                "2. Información sobre cirugías corporales\n"
                "3. Agenda una cita\n"
                "4. Promociones actuales\n"
                "5. Ubicación y horarios\n"
                "6. Hablar con un asesor"
            )

    # SUBMENÚ FACIAL
    if state == "facial_menu":
        if user_input == "1":
            return "👃 Rinoplastia: cirugía para mejorar la forma y función de la nariz. Tiempo de recuperación: 10-15 días."
        elif user_input == "2":
            return "👁️ Blefaroplastia: elimina el exceso de piel y bolsas en los párpados. Procedimiento ambulatorio."
        elif user_input == "3":
            return "🧓 Lifting facial: rejuvenece el rostro reduciendo arrugas y flacidez. Resultado natural."
        elif user_input == "4":
            return "🙂 Bichectomía: extracción de bolsas de Bichat para afinar el rostro. Rápida recuperación."
        elif user_input == "volver":
            user_states[user_id] = "main_menu"
            return get_response("", user_id)
        else:
            return "Opción no válida. Escribe un número del 1 al 4 o 'volver'."

    # SUBMENÚ CORPORAL
    if state == "corporal_menu":
        if user_input == "1":
            return "🧊 Liposucción: elimina grasa localizada. Ideal para abdomen, brazos y muslos."
        elif user_input == "2":
            return "👙 Abdominoplastia: corrige flacidez abdominal y elimina exceso de piel. Cicatriz baja."
        elif user_input == "3":
            return "🍑 Aumento de glúteos: mediante implantes o grasa propia (lipotransferencia)."
        elif user_input == "4":
            return "🖌️ Lipoescultura: combina liposucción con moldeado corporal. Resultados definidos."
        elif user_input == "volver":
            user_states[user_id] = "main_menu"
            return get_response("", user_id)
        else:
            return "Opción no válida. Escribe un número del 1 al 4 o 'volver'."

    return "Lo siento, no entendí tu respuesta. Escribe un número o 'volver'."
