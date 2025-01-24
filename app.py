from flask import Flask, jsonify, request
from employees.extractor import extract_news
from employees.content_creator import ContentCreator
from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory

app = Flask(__name__)

# Instancias de memoria
short_term_memory = ShortTermMemory()
long_term_memory = LongTermMemory(project_id=1)

# Rutas
@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a tu oficina virtual"})

@app.route('/extract_news', methods=['GET'])
def get_news():
    news = extract_news()
    for item in news:
        short_term_memory.add_context(item["title"])
    return jsonify({"news": news})

@app.route('/create_content', methods=['POST'])
def create_content():
    """
    Genera contenido basado en el estilo solicitado (social_media o article).
    """
    data = request.json
    style = data.get("style", "social_media")  # social_media o article
    context = short_term_memory.get_context()

    if not context:
        return jsonify({"error": "No hay contexto disponible. Extrae noticias primero."}), 400

    content_creator = ContentCreator(style=style)
    generated_content = content_creator.generate_content(context)

    long_term_memory.save_context(generated_content)

    return jsonify({"generated_content": generated_content})

@app.route('/save_memory', methods=['POST'])
def save_memory():
    context = short_term_memory.get_context()
    long_term_memory.save_context(context)
    short_term_memory.clear()
    return jsonify({"message": "Contexto guardado en memoria a largo plazo."})

if __name__ == '__main__':
    app.run(debug=True)