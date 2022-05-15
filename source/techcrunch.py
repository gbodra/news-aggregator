from core import HtmlSource, shortener_url


class TechCrunchHome(HtmlSource):
    def __init__(self, url: str) -> None:
        super().connect(url=url)
        self.top_news = []

    def fetch(self, limit: int):
        print("Fetching TechCrunch...")
        super().fetch(limit=limit)
        news = self.soup.find_all("a", "post-block__title__link")
        self.top_news = news[:limit]

    def to_string(self):
        parsed_news_list = [news.contents[0].strip() + " (" + shortener_url(news.attrs["href"]) + ")" for news in
                            self.top_news]
        message = "Techcrunch\n----------\n"
        message += "\n".join(parsed_news_list)
        return message

    def __repr__(self):
        return self.to_string()
