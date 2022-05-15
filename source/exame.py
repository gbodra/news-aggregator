from core import HtmlSource, shortener_url


class ExameHome(HtmlSource):
    def __init__(self, url: str) -> None:
        super().connect(url=url)
        self.top_news = []

    def fetch(self, limit: int):
        print("Fetching Exame...")
        super().fetch(limit=limit)
        news = self.soup.find_all("a", "touch-area")
        self.top_news = news[:limit]

    def to_string(self):
        protocol = self.url.find(":") + 3  # adiciona 3 para considerar as duas barras //
        base_url = self.url.find("/", protocol)
        parsed_news_list = [news.text.strip() + " (" + shortener_url(self.url[:base_url] + news.attrs["href"]) + ")" for
                            news in self.top_news]
        message = "Exame\n-----\n"
        message += "\n".join(parsed_news_list)
        return message

    def __repr__(self):
        return self.to_string()
