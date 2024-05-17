from flask import Flask, request
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'downloads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def receiver():
    # Check if request contains files
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']

    # Check if the file is present and has a filename
    if file.filename == '':
        return 'No selected file', 400

    # You can save the file or process it as needed
    # For example, saving the file to a specific directory
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                 
    # Optionally, you can perform additional processing here

    return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    