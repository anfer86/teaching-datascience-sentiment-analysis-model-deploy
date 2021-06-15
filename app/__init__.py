import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import app.helper
from app.helper import predict_from_sentenca, preprocessar_sentenca

app = Flask(__name__, template_folder='front-end')
CORS(app)

# Carregando o modelo (os scores)
print('Carregando o modelo')
model = pickle.load(open('app/model.pkl','rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/sentiment_analysis', methods=['POST'])
def predict():

	print('Recebendo os dados via POST')	
	data = request.get_json(force=True)
	print(data)

	sentenca = data['text']	
	print('Sentenca: ', sentenca)

	print('Realizando a predicao')
	prediction = predict_from_sentenca(sentenca, model, preprocessar_sentenca)

	print('Predição: ', prediction)
	print('Respondendo a requisição')
	output = jsonify(prediction)
	print(output)
	return output