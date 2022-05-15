from core import HtmlSource, shortener_url


class InfoMoneyHome(HtmlSource):
    def __init__(self, url: str) -> None:
        super().connect(url=url)
        self.top_news = []

    def fetch(self, limit: int):
        print("Fetching Info Money...")
        super().fetch(limit=limit)
        news = self.soup.find_all("span", "hl-title hl-title-2")
        news = [item for sublist in news for item in sublist.contents]
        self.top_news = news[:limit]

    def to_string(self):
        parsed_news_list = [news.text.strip() + " (" + shortener_url(news.attrs["href"]) + ")" for news in
                            self.top_news]
        message = "InfoMoney\n---------\n"
        message += "\n".join(parsed_news_list)
        return message

    def __repr__(self):
        return self.to_string()
