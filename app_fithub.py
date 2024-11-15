from flask import Flask, render_template, request, jsonify
from chatbot import FitMate

app = Flask(__name__)
chatbot = FitMate()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message")
    response = chatbot.handle_query(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
