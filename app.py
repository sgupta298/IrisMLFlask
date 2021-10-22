from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd
import json

app = Flask(__name__)

modelfile = 'models/final_prediction.pickle'

model = p.load(open(modelfile, 'rb'))

@app.route('/')
def main():
    return ('Predict Iris API')


@app.route('/api/', methods=['POST'])
def makecalc():
	j_data = request.get_json()

	prediction = np.array2string(model.predict(j_data))
	
	return jsonify({"Type": prediction})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')    