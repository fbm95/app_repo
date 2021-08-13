import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/greetings", methods=['GET'])
def greetings_controller():
  data = "Hello!"
  return jsonify(text=data)


# @app.route('/salutations', methods=['GET'])
# def salutations_controller():
#   data = "Salutations!"
#   return jsonify(text=data)


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
