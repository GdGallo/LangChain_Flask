from flask import Flask, jsonify, request
from employees.extractor import extract_news

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify ({"message":"Bienvenido a tu oficina virtual."})

@app.route('/extract_news',
           methods=['GET'])
def get_news():
    #Llamamos al exreactor de noticias
    news= extract_news()
    return jsonify({"news":news})

if __name__ == '__main__':
    app.run(debug=True)