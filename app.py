from flask import Flask, request, render_template, redirect, flash, session, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "nge4ev"


boggle_game = Boggle()

@app.route('/')
def show_homepage():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template("index.html", board=board)

@app.route("/check-word")
def check_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board,word)
    
    return jsonify({"result": response})

@app.route("/post-stats", methods=["POST"])
def post_stats():
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    playcount = session.get("playcount", 0)
    
    session["playcount"] = playcount + 1
    session["highscore"] = max(score, highscore)
    
    return jsonify(newHighscore= score > highscore)