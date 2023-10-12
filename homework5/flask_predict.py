import pickle

from flask import Flask
from flask import request
from flask import jsonify


# Model file and dv file
model_file = "model1.bin"
dv_file = "dv.bin"

# Read files function
def read_files(file_name):
    with open(file_name, 'rb') as file:
        result = pickle.load(file)
    return result

app = Flask('scoring')

@app.route('/predict', methods=['POST'])
def predict():
    custumer = request.get_json()

    model = read_files(model_file)
    dv = read_files(dv_file)

    X = dv.transform([custumer])
    y_pred = round(model.predict_proba(X)[0, 1], 3)

    result = {
        'credit_probability': float(y_pred)        
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
