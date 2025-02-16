from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get("input_data")
    return jsonify({"message": "Received", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
