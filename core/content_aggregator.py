import os
import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Source(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def to_string(self):
        pass


class HtmlSource(Source):
    def __init__(self):
        self.body = ""
        self.soup = ""
        self.url = ""

    def connect(self, url: str):
        self.url = url
        headers = {"User-agent": os.environ["USER_AGENT"]}
        self.body = requests.get(self.url, headers=headers).content

    def fetch(self, limit: int):
        self.soup = BeautifulSoup(self.body, 'html.parser')

    def to_string(self):
        pass
