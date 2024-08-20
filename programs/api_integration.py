from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('heatwave_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.json
    df = pd.DataFrame([data])
    
    # Make a prediction
    prediction = model.predict(df)
    
    # Convert the prediction to a readable format
    result = bool(prediction[0])
    
    return jsonify({"heatwave": result})

if __name__ == '__main__':
    app.run(debug=True)
