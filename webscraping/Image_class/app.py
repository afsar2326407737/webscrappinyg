from flask import Flask, render_template, request, redirect, url_for
import os
from predict_image import predict_image  # Import the prediction function

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)

    # Save the image to the upload folder
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_path)

    # Use the model to predict
    class_index, confidence = predict_image(image_path)

    # Clean up uploaded image (optional)
    os.remove(image_path)

    # Map the class index to the class name (replace these with actual class names)
    class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    result = class_names[class_index]

    # Render the result in the HTML page
    return render_template('index.html', result=result, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
