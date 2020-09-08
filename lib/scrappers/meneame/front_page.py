from lib.scrappers.base.base_scrapper import BaseScrapper
from lib.utils import fetch


class MeneameFrontPageScrapper(BaseScrapper):
    def __init__(self):
        self._target_uri = self._get_target_uri()

        super(MeneameFrontPageScrapper, self).__init__()

    def scrap(self, *args, **kwargs):
        soup = fetch.fetch_html(self._target_uri)

        scraps = []
        news = soup.select('.news-summary')[0:5]

        for n in news:
            header = n.select('h2')[0]
            title = header.text.strip()
            location = header.findChild('a').get('href')
            excerpt = ''

            scraps.append([title, excerpt, location])

        return scraps

    def _get_target_uri(self):
        return 'https://www.meneame.net/'
