"""SF Treasures - The All-Women Hackathon San Francisco 9/10/16"""

from flask import Flask, render_template, request, flash, redirect, session, jsonify
<<<<<<< HEAD
# from Jinja2 import StrictUndefined
from model import Leader, connect_to_db
=======
from Jinja2 import StrictUndefined

import geojson
>>>>>>> aroseartist-master
import json
import os
import requests
import sys
from helpers import send_sms
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.secret_key = os.environ.get('FLASK_SECRET_KEY')
<<<<<<< HEAD

=======
>>>>>>> aroseartist-master

# Ensures undefined variables in jinja raise an error
# app.jinja_env.undefined = StrictUndefined
# allows html to reload without restarting server
app.jinja_env.auto_reload = True

###############################################################################


@app.route('/')
def show_homepage():
    """Show homepage."""


    return render_template("homepage.html")


@app.route('/game_time')
def show_gamepage():
    """Show progress of game being played."""

    neighborhood = request.args.get("neighborhood")
    num_clues = int(request.args.get("clues"))
    team_name = request.args.get("teamName")
    #list of unicode items
    phone_number_list = request.args.getlist("phoneNumber")

    phone_number = "1"+str(phone_number_list[0])+str(phone_number_list[1])+str(phone_number_list[2])

    session["phone_number"] = phone_number

    # send_sms(session["phone_number"], "Clue 1")
    # print "Success! Look out for text messge."

    #query database for leaderboard information and pass object to game.html
    leaderboard = Leader.query.all()

<<<<<<< HEAD
    return render_template("game.html", leaderboard=leaderboard, team_name=team_name, num_clues=num_clues)
=======
    return render_template("game.html")
>>>>>>> aroseartist-master


@app.route('/results')
def show_winner():
    """Display winner."""

    return render_template("results.html")
    

##########################################################################

# # Listening or requests
if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0")

