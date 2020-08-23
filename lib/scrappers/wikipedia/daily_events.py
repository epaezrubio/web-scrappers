import datetime
import locale
import time
from collections import defaultdict

from lib.scrappers.base.base_scrapper import BaseScrapper

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
        pass

    def _get_target_uri(self):
        locale.setlocale(locale.LC_TIME, self._locale)

        return 'https://{}.wikipedia.org/wiki/{}'.format(
            self._subdomain, date_handlers[self._subdomain](self._date))
