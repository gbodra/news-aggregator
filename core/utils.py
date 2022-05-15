import pyshorteners


def shortener_url(url: str):
    type_tiny = pyshorteners.Shortener()

    return type_tiny.tinyurl.short(url)
