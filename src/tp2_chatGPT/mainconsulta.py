# Importa readline para manejar el historial de entradas del usuario
import readline
# Importa la biblioteca de OpenAI para interactuar con su API
import openai

# Maneja la compatibilidad del módulo readline en distintos sistemas
try:
    import readline
except ImportError:
    import pyreadline as readline  # pyreadline es usado en Windows

# Asigna tu clave API para autenticar las peticiones a OpenAI
openai.api_key = "tu-api-key"

# Función para obtener una consulta del usuario desde la terminal
def obtener_consulta():
    try:
        # Solicita al usuario que ingrese su mensaje
        consulta = input("Ingrese su consulta: ").strip()

        # Verifica que el usuario haya ingresado algo
        if not consulta:
            raise ValueError("La consulta no puede estar vacía.")

        # Agrega la consulta al historial (útil para teclas ↑ ↓)
        readline.add_history(consulta)

        # Muestra la consulta del usuario por pantalla
        print(f"You: {consulta}")
        return consulta
    except Exception as e:
        # Muestra errores relacionados con la entrada del usuario
        print(f"Error en la entrada del usuario: {e}")
        return None

# Procesa la consulta del usuario para estructurarla como mensaje para la API
def procesar_consulta(consulta):
    try:
        # Define los mensajes en el formato requerido por ChatGPT
        mensajes = [
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": consulta}
        ]
        return mensajes
    except Exception as e:
        # Muestra errores en la preparación de los mensajes
        print(f"Error al preparar los mensajes: {e}")
        return None

# Función que envía la consulta a ChatGPT y muestra la respuesta
def invocar_chatgpt(mensajes):
    try:
        # Realiza la petición a la API de ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Especifica el modelo
            messages=mensajes,      # Mensajes preparados
            temperature=1,          # Aleatoriedad de la respuesta
            max_tokens=150,         # Límite de tokens de respuesta
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Extrae y muestra la respuesta de ChatGPT
        respuesta_texto = response.choices[0].message["content"]
        print(f"chatGPT: {respuesta_texto}")
    except Exception as e:
        # Muestra errores al invocar la API
        print(f"Error al invocar chatGPT: {e}")

# Función principal que ejecuta el ciclo de interacción con el usuario
def main():
    while True:
        # Obtiene la consulta del usuario
        consulta = obtener_consulta()
        if not consulta:
            continue
        # Procesa la consulta en formato para la API
        mensajes = procesar_consulta(consulta)
        if not mensajes:
            continue
        # Envía la consulta a ChatGPT
        invocar_chatgpt(mensajes)

# Llama a la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
