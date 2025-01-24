from flask import Flask, jsonify, request, render_template
from employees.extractor import extract_news
from employees.content_creator import ContentCreator
from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory

app = Flask(__name__)

# Instancias de memoria
short_term_memory = ShortTermMemory()
long_term_memory = LongTermMemory(project_id=1)

# Rutas de la interfaz
@app.route('/')
def home():
    return render_template("index.html")

# Rutas de la API
@app.route('/extract_news', methods=['GET'])
def get_news():
    try:
        news = extract_news()
        for item in news:
            short_term_memory.add_context(item["title"])
        return jsonify({"news": news})
    except Exception as e:
        return jsonify({"error": f"Error al extraer noticias: {str(e)}"}), 500

@app.route('/create_content', methods=['POST'])
def create_content():
    try:
        data = request.json
        style = data.get("style", "social_media")
        context = short_term_memory.get_context()

        if not context:
            return jsonify({"error": "No hay contexto disponible. Extrae noticias primero."}), 400

        content_creator = ContentCreator(style=style)
        generated_content = content_creator.generate_content(context)
        return jsonify({"generated_content": generated_content})
    except Exception as e:
        return jsonify({"error": f"Error al generar contenido: {str(e)}"}), 500

@app.route('/save_memory', methods=['POST'])
def save_memory():
    try:
        context = short_term_memory.get_context()
        if not context:
            return jsonify({"error": "No hay contexto disponible para guardar."}), 400

        long_term_memory.save_context(context)
        short_term_memory.clear()
        return jsonify({"message": "Contexto guardado en memoria a largo plazo."})
    except Exception as e:
        return jsonify({"error": f"Error al guardar memoria: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
