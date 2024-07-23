"""
    Title: metaPy
    Author: Carlos Mena
    Version: 2.0
    Description: Python service for "image metadata deletion", using Flask.
    This service actually generates a copy with the same base data, 
     excluding its metadata.
    
"""
from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Decorator with path and method
@app.route('/remove-metadata', methods=['POST'])
def remove_metadata():
    try:
        # Making sure file is provided
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Open the image
        image = Image.open(file.stream)

        # Generating 
        data = list(image.getdata())
        image_without_metadata = Image.new(image.mode, image.size)
        image_without_metadata.putdata(data)

        # Save image to a bytes buffer
        buffer = BytesIO()
        image_without_metadata.save(buffer, format=image.format)
        buffer.seek(0)

        # Return the image without metadata
        return buffer.getvalue(), 200, {
            'Content-Type': 'image/{}'.format(image.format.lower()),
            'Content-Disposition': 'attachment; filename={}'.format(file.filename)
        }

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)