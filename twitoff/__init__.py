"""The first file that is run when running the twitoff package"""
from .app import create_app
from .models import User, Tweet

APP = create_app()

