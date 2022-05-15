from core import HtmlSource, shortener_url


class WiredHome(HtmlSource):
    def __init__(self, url: str) -> None:
        super().connect(url=url)
        self.top_news = []

    def fetch(self, limit: int):
        print("Fetching Wired...")
        super().fetch(limit=limit)
        news = self.soup.find_all("a", "summary-item__hed-link")
        # news = [item for sublist in news for item in sublist.contents]
        self.top_news = news[:limit]

    def to_string(self):
        # self.url[:-1] para remover a ultima barra da url
        parsed_news_list = [news.text.strip() + " (" + shortener_url(self.url[:-1] + news.attrs["href"]) + ")" for news
                            in self.top_news]
        message = "Wired\n-----\n"
        message += "\n".join(parsed_news_list)
        return message

    def __repr__(self):
        return self.to_string()
