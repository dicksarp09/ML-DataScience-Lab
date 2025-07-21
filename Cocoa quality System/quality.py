from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from detect import run_detection

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        if file.filename == '':
            return "No selected file"

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Run detection
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.jpg')
        run_detection(filepath, output_path)

        return render_template("index.html", uploaded=True, image_path='static/output.jpg')

    return render_template("index.html", uploaded=False)

if __name__ == "__main__":
    app.run(debug=True)
