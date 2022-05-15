import os
import requests
import urllib.parse


def send_telegram_message(message: str):
    params = "chat_id=" + os.environ["CHAT_ID"] + "&text=" + urllib.parse.quote(message)\
             + "&parse_mode=Markdown&disable_web_page_preview=true"
    url = os.environ["TG_URL"] + os.environ["TG_TOKEN"] + "/sendMessage?" + params

    response = requests.get(url)

    return response.json()
