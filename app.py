from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Load intents from the JSON file
with open("intents.json", "r") as file:
    intents = json.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower() if data else ""

    # Default reply if no match found
    reply = (
        "I'm not sure how to answer that yet. 🤖 "
        "Try asking me Python-related questions!"
    )

    # Loop through intents to find a matching pattern
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_message:
                reply = random.choice(intent["responses"])
                break  # Stop once a match is found
        if reply != (
            "I'm not sure how to answer that yet. 🤖 "
            "Try asking me Python-related questions!"
        ):
            break

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
