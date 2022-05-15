import os
import praw
from core.content_aggregator import Source


class RedditSource(Source):
    def connect(self):
        self.reddit_con = praw.Reddit(client_id=os.environ["REDDIT_CLIENT_ID"],
                                      client_secret=os.environ["REDDIT_SECRET"],
                                      grant_type_access='client_credentials',
                                      user_agent='script/1.0')
        return self.reddit_con

    def fetch(self):
        pass


class RedditFront(RedditSource):
    def __init__(self) -> None:
        self.reddit_con = super().connect()
        self.hot_submissions = []

    def fetch(self, limit: int):
        self.hot_submissions = self.reddit_con.front.new(limit=limit)

    def __repr__(self):
        urls = []
        for submission in self.hot_submissions:
            urls.append(submission.title)

        return '\n'.join(urls)
