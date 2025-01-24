import openai
import os

# Configuración de la API de OpenAI
openai.api_key = "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"
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

        try:
            # Llamada a la nueva API de OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Eres un generador de contenido profesional."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7,
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            return f"Error al generar contenido: {e}"
