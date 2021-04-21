"""Getting tweets and users from the Twitter DB"""
import tweepy
import spacy
import os
from .models import User, DB, Tweet

TWITTER_API_KEY="6enLGJXRWzsORKwclaGEPm2H9"
TWITTER_API_KEY_SECRET="OyFT4y8g5zIhvnzTbA8sTOD215GsspKg3VQ0qsGk1yO3S12bNt"
TWITTER_AUTH = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
TWITTER = tweepy.API(TWITTER_AUTH)

# loads word to vext model
# nlp = spacy.load("my_model")

def vectorize_tweet(tweet_text):
    # return nlp(tweet_text).vector
    pass

def add_or_update_user(username):
    """
    Gets twitter user and tweets from twitter DB
    Gets user by "username" parameter.
    """
    try:
        # gets back twitter user object
        twitter_user = TWITTER.get_user(username)
        # Either updates or adds user to our DB
        db_user = (User.query.get(twitter_user.id)) or User(
            id=twitter_user.id, name=username)
        DB.session.add(db_user)  # Add user if don't exist
        # Grabbing tweets from "twitter_user"
        tweets = twitter_user.timeline(
            count=200,
            exclude_replies=True,
            include_rts=False,
            tweet_mode="Extended",
            since_id=db_user.newest_tweet_id
        )

        print(tweets)

        if tweets:
            db_user.newest_tweet_id = tweets[0].id

        # tweets is a list of tweet objects
        # for tweet in tweets:
        #     # type(tweet) == object
        #     tweet_vector = vectorize_tweet(tweet.text)
        #     db_tweet = Tweet(
        #         id=tweet.id,
        #         text=tweet.text,
        #         vect=tweet_vector
        #     )
        #     db_user.tweets.append(db_tweet)
        #     DB.session.add(db_tweet)

    except Exception as e:
        print("Error processing {}: {}".format(username, e))

    else:
        DB.session.commit()



""" Code to test the model
>>> from twitoff.models import User, DB
>>> from twitoff.twitter import add_or_update_user
>>> add_or_update_user("elonmusk")
>>> User.query.all()
>>> User.query.all()[0]
>>> user = User.query.all()[0]
>>> user.tweets
"""