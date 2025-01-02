from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/<path:filename>')
def serve_template_file(filename):
    return send_from_directory('templates', filename)

@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files.get('image')
    language = request.form.get('language', 'sample')
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return render_template('upload.html', uploaded_image=filename)
    return redirect(url_for('index'))

@app.route('/extract-text', methods=['POST'])
def extract_text():
    image_name = request.form.get('image_name')
    language = request.form.get('language', 'sample')
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
    if os.path.exists(image_path):
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img, lang=language)
        return render_template('extract-text.html', extracted_text=extracted_text, image_name=image_name)
    return redirect(url_for('index'))

@app.route('/download-text', methods=['POST'])
def download_text():
    text = request.form.get('extracted_text')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'extracted-text.txt')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return send_file(file_path, as_attachment=True, download_name='extracted-text.txt')

if __name__ == '__main__':
    app.run(debug=True)