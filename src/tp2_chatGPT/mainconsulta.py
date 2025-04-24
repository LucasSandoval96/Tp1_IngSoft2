"""Este módulo permite realizar consultas a la API de ChatGPT e imprimir respuestas en consola."""

import readline  # módulo estándar
import openai    # módulo externo

# Asigna tu clave API de OpenAI
openai.api_key = "tu-api-key"

def obtener_consulta():
    """Solicita una consulta al usuario, valida que no esté vacía y la imprime."""
    try:
        consulta = input("Ingrese su consulta: ").strip()
        if not consulta:
            raise ValueError("La consulta no puede estar vacía.")
        readline.add_history(consulta)
        print(f"You: {consulta}")
        return consulta
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error inesperado en la entrada del usuario: {e}")
        return None

def procesar_consulta(consulta):
    """Prepara los mensajes para enviarlos a la API de ChatGPT."""
    try:
        mensajes = [
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": consulta}
        ]
        return mensajes
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error al preparar los mensajes: {e}")
        return None

def invocar_chatgpt(mensajes):
    """Envía los mensajes a ChatGPT y muestra la respuesta recibida."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=mensajes,
            temperature=1,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        respuesta_texto = response.choices[0].message["content"]
        print(f"chatGPT: {respuesta_texto}")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error al invocar chatGPT: {e}")

def main():
    """Ciclo principal que obtiene consultas, procesa y comunica con ChatGPT."""
    while True:
        consulta = obtener_consulta()
        if not consulta:
            continue
        if consulta.lower() in ["salir", "exit"]:
            print("Saliendo del programa.")
            break
        mensajes = procesar_consulta(consulta)
        if not mensajes:
            continue
        invocar_chatgpt(mensajes)

if __name__ == "__main__":
    main()
