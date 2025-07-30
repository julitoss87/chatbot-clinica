def get_response(message):
    message = message.lower()

    if "hola" in message:
        return "Hola 👋 Bienvenido a Clínica BellaForma. ¿En qué podemos ayudarte hoy?"

    elif "cita" in message:
        return "¿Deseas agendar una cita presencial o virtual? Por favor escribe 'presencial' o 'virtual'."

    elif "presencial" in message:
        return "Perfecto. Por favor indícanos tu nombre y el procedimiento de interés."

    elif "virtual" in message:
        return "Genial. Podemos agendar tu cita virtual. Por favor dinos tu nombre y el procedimiento de interés."

    elif "gracias" in message:
        return "Con gusto 😊. Si necesitas algo más, estamos atentos."

    else:
        return "Gracias por escribirnos. En breve un asesor se comunicará contigo."