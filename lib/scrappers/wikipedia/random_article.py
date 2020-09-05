import time

from bs4 import BeautifulSoup

from lib.scrappers.base.base_scrapper import BaseScrapper
from lib.utils import fetch


locale_article_url = {
    'de': 'Spezial:Zuf%C3%A4llige_Seite',
    'en': 'Special:Random',
    'es': 'Especial:Aleatoria',
}


class WikipediaRandomArticleScrapper(BaseScrapper):
    def __init__(self, subdomain='en'):
        self._subdomain = subdomain
        self._target_uri = self._get_target_uri()

        super(WikipediaRandomArticleScrapper, self).__init__()

    def scrap(self, *args, **kwargs):
        location = fetch.fetch_header(self._target_uri, 'location')
        soup = fetch.fetch_html(location)

        title = soup.select('#firstHeading')[0].text
        paragraphs = soup.select('#bodyContent p')
        first_paragraph = paragraphs[0].text if paragraphs else ''

        return [title, first_paragraph, location]



    def _get_target_uri(self):
        return 'https://{}.wikipedia.org/wiki/{}'.format(
            self._subdomain, locale_article_url[self._subdomain])
