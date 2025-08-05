from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, secure world!"})

@app.route("/greet", methods=["POST"])
def greet():
    name = request.json.get("name", "Guest")
    return jsonify({"greeting": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(debug=False)
