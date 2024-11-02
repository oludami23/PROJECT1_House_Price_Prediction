from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

# Initialize Flask app
app = Flask(__name__)

# Load the trained model (assuming you saved it in the new format)
model = tf.keras.models.load_model('house_price_nn_model.keras')

# Define the route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract features from JSON data
        features = np.array(data['features']).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(features).flatten()[0]

        # Return the prediction in JSON format
        return jsonify({'SalePrice': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
