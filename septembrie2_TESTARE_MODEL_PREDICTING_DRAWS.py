import pickle

import pandas as pd
from pgmpy.inference import VariableElimination

# Încărcare model salvat
with open('trained_model_bayesian_network_9_AUGUST.pkl', 'rb') as file:
    model = pickle.load(file)

# Creare obiect de inferență
inference = VariableElimination(model)

test_data = pd.read_csv("test_data_9_AUGUST_CORECTAT.csv")

# Definirea funcției de predicție prin eșantionare
def predict_with_inference(data_row):
    evidence = data_row.to_dict()
    evidence_inference = {key: value if key in model.nodes() else value for key, value in evidence.items() if
                          key in model.nodes() and key != 'result'}
    result = inference.map_query(variables=['result'], evidence=evidence_inference)
    return result['result']

# Aplicarea funcției de predicție pentru fiecare rând din setul de date
test_data['Predicted_result'] = test_data.apply(predict_with_inference, axis=1)

# Compararea predicțiilor cu valorile reale
correct_predictions = sum(test_data['result'] == test_data['Predicted_result'])
total_predictions = len(test_data)
accuracy = correct_predictions / total_predictions
print(f"Accuracy: {accuracy * 100:.2f}%")

# Aplicarea funcției de predicție pentru fiecare rând din setul de date și afișarea rezultatului
for index, row in test_data.iterrows():
    predicted_result = predict_with_inference(row)
    actual_result = row['result']
    print(f"Row {index}: Predicted result = {predicted_result}, Actual result = {actual_result}")
    test_data.at[index, 'Predicted_result'] = predicted_result
