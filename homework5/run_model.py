import pickle

# Load model
def load_model():
    with open("model1.bin", 'rb') as f_model:
        model = pickle.load(f_model)
    return model
    
# Load dv
def load_dv():
    with open("dv.bin", 'rb') as f_dv:
        dv = pickle.load(f_dv)
    return dv

if __name__ == "__main__":
    model = load_model()
    dv = load_dv()

    custumer = {"job": "retired", "duration": 445, "poutcome": "success"}

    X = dv.transform([custumer])
    result = round(model.predict_proba(X)[0,1], 3)
    print(result)


