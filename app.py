from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chat import get_response  # Assuming you have implemented this function

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.json.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    response = get_response(message)
    response_text = response.text
    return jsonify({'response': response_text})

if __name__ == "__main__":
    app.run(debug=True)
