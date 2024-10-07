from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import json

# Initialize the Flask app and specify the static folder
app = Flask(__name__)

# Load the pre-trained model
model = load_model('plant_disease_prediction_model.h5')

# Load class indices mapping (this is created from your training step)
with open('class_indices.json') as f:
    class_indices = json.load(f)

# Route to load the homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Route to load the index page
# @app.route('/')
# def index():
#     return render_template('index.html')

# Prediction route to handle image uploads and return the prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('result.html', prediction="No file uploaded")
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('result.html', prediction="No file selected")

    try:
        # Load and preprocess the image
        image = Image.open(file)
        image = image.resize((224, 224))  # Resize as per your model's input size
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        image = image / 255.0  # Normalize the image (as you did during training)

        # Get model predictions
        prediction = model.predict(image)
        predicted_class_index = np.argmax(prediction, axis=1)[0]

        # Get human-readable label
        predicted_class_name = class_indices[str(predicted_class_index)]

        # Return the result page with the prediction
        return render_template('result.html', prediction=predicted_class_name)
    
    except Exception as e:
        print(f"Error: {str(e)}")  # Log error for debugging
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
