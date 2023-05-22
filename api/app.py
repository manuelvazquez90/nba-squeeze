from flask import Flask

from services.games import *

app = Flask(__name__)

@app.route("/api/games", methods=['GET'])
def data_games():
    data = Games.run()
    return data, 200

if __name__ == "__main__":
    app.run(debug=True)