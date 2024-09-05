from flask import Flask, request, jsonify, render_template
import pickle

from pgmpy.inference import VariableElimination

app = Flask(__name__)

# Încărcarea modelului antrenat
with open('trained_model_bayesian_network_9_AUGUST.pkl', 'rb') as file:
    model = pickle.load(file)

# Creare obiect de inferență
inference = VariableElimination(model)


# Definirea funcției de predicție
def predict_result(data_row):
    evidence = {key: value for key, value in data_row.items() if key in model.nodes() and key != 'result'}
    result = inference.map_query(variables=['result'], evidence=evidence)
    return result['result']


# Ruta principală care servește pagina web
@app.route('/')
def index():
    return render_template('index.html')


# Ruta pentru predicție
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    result = predict_result(data)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
