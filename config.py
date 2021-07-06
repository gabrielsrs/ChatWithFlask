from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Config:
    """Set Flask configuration vars from .env file."""

    # Load in enviornemnt variables
    TESTING = getenv('TESTING')
    FLASK_DEBUG = getenv('FLASK_DEBUG')
    SECRET_KEY = getenv('SECRET_KEY')
    SERVER = getenv('SERVER')
    PORT = getenv('PORT')
