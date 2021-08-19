import os

from flask import Flask

app = Flask(__name__)


@app.route("/greetings", methods=['GET'])
def greetings_controller():
  data = "Hello!"
  return data


@app.route('/salutations', methods=['GET'])
def salutations_controller():
  data = "Salutations!"
  return data


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 80)))
