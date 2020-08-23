import datetime

from lib.scrappers.wikipedia.daily_events import WikipediaDailyEventScrapper


def test_target_uri_de():
    scrapper = WikipediaDailyEventScrapper(subdomain='de',
                                           date=datetime.datetime(2020, 8, 10),
                                           date_locale='de_DE')
    assert scrapper._target_uri == 'https://de.wikipedia.org/wiki/10._August'


def test_target_uri_es():
    scrapper = WikipediaDailyEventScrapper(subdomain='es',
                                           date=datetime.datetime(2020, 8, 10),
                                           date_locale='es_ES')
    assert scrapper._target_uri == 'https://es.wikipedia.org/wiki/10_de_agosto'


def test_target_uri_en():
    scrapper = WikipediaDailyEventScrapper(subdomain='en',
                                           date=datetime.datetime(2020, 8, 10),
                                           date_locale='en_US')
    assert scrapper._target_uri == 'https://en.wikipedia.org/wiki/August_10'
