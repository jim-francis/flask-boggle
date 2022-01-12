from flask import Flask, request, render_template, redirect, flash, session
from boggle import Boggle

app = Flask(__name__)

boggle_game = Boggle()

@app.route('/')
def show_homepage():
    return render_template("index.html")