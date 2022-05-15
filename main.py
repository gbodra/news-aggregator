from core import App, send_telegram_message
from source import TechCrunchHome, TheVergeHome, TheHustleHome, ExameHome
from source import InfoMoneyHome, WiredHome, StartupsHome, FastCompanyHome


if __name__ == '__main__':
    app = App()
    LIMIT = 5
    message = ""

    tc = TechCrunchHome(url="https://techcrunch.com/")
    tc.fetch(limit=LIMIT)
    message += tc.to_string() + "\n\n"

    tv = TheVergeHome(url="https://www.theverge.com/")
    tv.fetch(limit=LIMIT)
    message += tv.to_string() + "\n\n"

    th = TheHustleHome(url="https://thehustle.co/")
    th.fetch(limit=LIMIT)
    message += th.to_string() + "\n\n"

    ex = ExameHome(url="https://exame.com/exame-in/")
    ex.fetch(limit=LIMIT)
    message += ex.to_string() + "\n\n"

    im = InfoMoneyHome(url="https://www.infomoney.com.br/ultimas-noticias/")
    im.fetch(limit=LIMIT)
    message += im.to_string() + "\n\n"

    wr = WiredHome(url="https://www.wired.com/")
    wr.fetch(limit=LIMIT)
    message += wr.to_string() + "\n\n"

    st = StartupsHome(url="https://startups.com.br/noticias/")
    st.fetch(limit=LIMIT)
    message += st.to_string() + "\n\n"

    fc = FastCompanyHome(url="https://www.fastcompany.com/")
    fc.fetch(limit=LIMIT)
    message += fc.to_string() + "\n\n"

    send_telegram_message(message)
    # print(message)
