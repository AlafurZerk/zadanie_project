from flask import Flask, request, jsonify
from PIL import Image
import base64
from io import BytesIO


app = Flask(__name__)

@app.route('/image', methods=['POST'])
def upload_image():
    data = request.json
    extension = data['extension']
    size = float(data['size'].replace(' KB', ''))
    description = data['description']
    title = data['title']
    tags = data['tags']
    base64_image = data['base64']

    if size > 1024:
        return jsonify({"error": "Размер картинки больше чем 1МБ"}), 413

    try:
        image_data = base64.b64decode(base64_image.split(',')[1])
        image = Image.open(BytesIO(image_data))
        if image.format.lower() != extension:
            return jsonify({"error": "Формат не соответствует"}), 415
    except Exception as e:
        return jsonify({"error": "Ошибка обработки"}), 400

    image_path = f'gallery/{title}.{extension}'
    with open(image_path, 'wb') as f:
        f.write(image_data)