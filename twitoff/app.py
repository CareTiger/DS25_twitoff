"""This is what brings the application together"""
from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():
    """
    The main app function for twitoff.
    Brings everything together.
    """
    # __name__ is the name of the current path module
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        # Drops everything from DB
        DB.drop_all()
        # Creates DB
        DB.create_all()
        insert_example_users()
        insert_example_tweets()
        return render_template('base.html', title="Home")

    @ app.route('/update')
    def hola():
        return "Update, Twitoff"

    @ app.route('/reset')
    def salut():
        return "Reset, Twitoff"

    return app

def insert_example_users():
    """Will insert two hypothetical users we've made"""
    nick = User(id=1, name="nick")
    elon = User(id=2, name="elonmusk")
    DB.session.add(nick)
    DB.session.add(elon)
    print("Created users")
    DB.session.commit()

def insert_example_tweets():
    """Will insert hypothetical tweets"""
    tweet1 = Tweet(id=1, text="THis is my FIRST tweet", user_id=1)
    tweet2 = Tweet(id=2, text="THis is my SECOND tweet", user_id=1)
    tweet3 = Tweet(id=3, text="THis is my THIRD tweet", user_id=1)
    tweet4 = Tweet(id=4, text="THis is my FOURTH tweet", user_id=2)
    tweet5 = Tweet(id=5, text="THis is my FIFTH tweet", user_id=2)
    tweet6 = Tweet(id=6, text="THis is my SIXTH tweet", user_id=2)
    tweet7 = Tweet(id=7, text="THis is my SEVENTH tweet", user_id=2)
    DB.session.add(tweet1)
    DB.session.add(tweet2)
    DB.session.add(tweet3)
    DB.session.add(tweet4)
    DB.session.add(tweet5)
    DB.session.add(tweet6)
    DB.session.add(tweet7)
    print("Created sample tweets")
    DB.session.commit()    