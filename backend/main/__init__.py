import os
from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    load_dotenv()
    return app
