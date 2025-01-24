import openai
import os

# Configuración de la API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class ContentCreator:
    def __init__(self, style="social_media"):
        self.style = style

    def generate_content(self, context):
        """
        Genera contenido según el estilo especificado (social_media o article).
        """
        if self.style == "social_media":
            prompt = f"Crea un mensaje atractivo y breve para redes sociales basado en el siguiente contenido: {context}"
        elif self.style == "article":
            prompt = f"Escribe un artículo detallado basado en el siguiente contenido: {context}"
        else:
            raise ValueError("Estilo no soportado. Usa 'social_media' o 'article'.")
        
        # Llamada a OpenAI para generar contenido
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-0613",  # Asegúrate de usar un modelo válido como gpt-4-0613 o gpt-3.5-turbo-0613
                messages=[
                    {"role": "system", "content": "Eres un generador de contenido profesional."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"Error al generar contenido: {e}"
