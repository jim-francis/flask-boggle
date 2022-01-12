from flask import Flask, request, render_template, redirect, flash, session
from boggle import Boggle

app = Flask(__name__)

boggle_game = Boggle()

@app.route('/')
def show_homepage():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template("index.html", board=board)