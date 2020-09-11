from lib.scrappers.base.base_scrapper import BaseScrapper
from lib.utils import fetch


class GenbetaLastPostsScrapper(BaseScrapper):
    def __init__(self):
        self._target_uri = self._get_target_uri()

        super(GenbetaLastPostsScrapper, self).__init__()

    def scrap(self, *args, **kwargs):
        soup = fetch.fetch_html(self._target_uri)

        scraps = []
        articles = soup.select('.abstract-content')[0:5]

        for a in articles:
            title = a.select('.abstract-title')[0]
            title_text = title.text.strip()
            location = title.findChild('a').get('href')
            excerpt = a.select('.abstract-excerpt')[0].findChild('p').text.strip()

            scraps.append([title_text, excerpt, location])

        return scraps

    def _get_target_uri(self):
        return 'https://www.genbeta.com'
