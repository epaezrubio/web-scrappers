import requests
from bs4 import BeautifulSoup


def fetch_html(target):
    response = requests.get(target, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, "html.parser")

    return soup


def fetch_header(target, header):
    response = requests.get(target, allow_redirects=False)

    return response.headers.get(header)