from flask import Flask, jsonify, request
from employees.extractor import extract_news
from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory

app = Flask(__name__)

# Instancias de memoria
short_term_memory = ShortTermMemory()
long_term_memory = LongTermMemory(project_id=1)  # Ejemplo: ID del proyecto

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a tu oficina virtual"})

@app.route('/extract_news', methods=['GET'])
def get_news():
    news = extract_news()
    for item in news:
        short_term_memory.add_context(item["title"])
    return jsonify({"news": news})

@app.route('/save_memory', methods=['POST'])
def save_memory():
    context = short_term_memory.get_context()
    long_term_memory.save_context(context)
    short_term_memory.clear()
    return jsonify({"message": "Contexto guardado en memoria a largo plazo."})

if __name__ == '__main__':
    app.run(debug=True)