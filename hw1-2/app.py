from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Function to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    lag_1 = data['lag_1']
    lag_2 = data['lag_2']
    volume = data['volume']
    
    # Scaling the input
    input_scaled = scaler.transform([[lag_1, lag_2, volume]])
    input_selected = selector.transform(input_scaled)
    
    # Make the prediction
    prediction = model.predict(input_selected)
    return jsonify({'predicted_close': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
