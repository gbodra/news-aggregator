import os
from dotenv import load_dotenv


class App:
    def __init__(self):
        load_dotenv()
        self.MEDIUM_TOKEN = os.environ["MEDIUM_TOKEN"]
        self.REDDIT_CLIENT_ID = os.environ["REDDIT_CLIENT_ID"]
        self.REDDIT_SECRET = os.environ["REDDIT_SECRET"]
