import datetime
import locale
import re
import time
from collections import defaultdict

from bs4 import BeautifulSoup

from lib.scrappers.base.base_scrapper import BaseScrapper
from lib.utils import fetch

date_handlers = defaultdict(lambda: lambda x: x.strftime('%B_%d'))
date_handlers['de'] = lambda x: x.strftime('%d._%B')
date_handlers['es'] = lambda x: x.strftime('%d_de_%B')


class WikipediaDailyEventScrapper(BaseScrapper):
    def __init__(self, subdomain='en', date=datetime.datetime.now(),
                 date_locale='en_US'):
        self._subdomain = subdomain
        self._date = date
        self._locale = '{}.utf8'.format(date_locale)

        self._target_uri = self._get_target_uri()

        super(WikipediaDailyEventScrapper, self).__init__()

    def scrap(self, *args, **kwargs):
        soup = fetch.fetch_html(self._target_uri)
        bullets = soup.select('#bodyContent li')

        whitelist = kwargs.get('whitelist', [])
        blacklist = kwargs.get('blacklist', [])

        results = {}

        for bullet in bullets:
            text = bullet.text.strip().lower()

            if not re.match("^\d+", text):
                continue

            if any(word.lower() in text for word in blacklist):
                continue

            if any(word.lower() in text for word in whitelist):
                bullet_section = bullet.parent.find_previous_sibling('h2')

                if not bullet_section:
                    continue

                bullet_title = bullet_section.contents[0].get_text()

                if bullet_title not in results:
                    results[bullet_title] = []

                results[bullet_title].append(text)

        return results

    def _get_target_uri(self):
        locale.setlocale(locale.LC_TIME, self._locale)

        return 'https://{}.wikipedia.org/wiki/{}'.format(
            self._subdomain, date_handlers[self._subdomain](self._date))
