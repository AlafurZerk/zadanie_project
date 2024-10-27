from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'static/index.html')

@app.route('/jsonEndpoint')
def json_endpoint():
    return jsonify({"message": "Hello World"}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
