from core import HtmlSource, shortener_url


class TheVergeHome(HtmlSource):
    def __init__(self, url: str) -> None:
        super().connect(url=url)
        self.top_news = []

    def fetch(self, limit: int):
        print("Fetching The Verge...")
        super().fetch(limit=limit)
        news = self.soup.find_all("h2", "c-entry-box--compact__title")
        news = [child.contents[0] for child in news]
        self.top_news = news[:limit]

    def to_string(self):
        parsed_news_list = [news.text.strip() + " (" + shortener_url(news.attrs["href"]) + ")" for news in
                            self.top_news]
        message = "The Verge\n---------\n"
        message += "\n".join(parsed_news_list)
        return message

    def __repr__(self):
        return self.to_string()
