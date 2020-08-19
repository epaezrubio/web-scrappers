import requests

from bs4 import BeautifulSoup


def fetch_html(target):
    response = requests.get(target)
    soup = BeautifulSoup(response.text, "html.parser")

    return soup
