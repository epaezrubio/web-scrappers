from lib.scrappers.base.base_scrapper import BaseScrapper
from lib.utils import fetch


class SteamGameDeals(BaseScrapper):
    def __init__(self, currency="€"):
        self._target_uri = self._get_target_uri()
        self._currency = currency

        super(SteamGameDeals, self).__init__()

    def scrap(self, *args, **kwargs):
        soup = fetch.fetch_html(self._target_uri)

        scraps = {}
        deals = soup.select('.search_result_row')[0:15]

        for d in deals:
            price = d.select('.search_price')[0].text.strip()

            if not price or price == 'Free to Play':
                continue

            discount = d.select('.search_discount')[0].text.strip()

            if discount not in scraps:
                scraps[discount] = []

            title = d.select('.title')[0].text.strip()
            price_diff = "{} -> {}".format(*[
                "{}{}".format(p, self._currency)
                for p in price.split(self._currency)[0:2]
            ])

            scraps[discount].append("{} ({})".format(title, price_diff))

        return scraps

    def _get_target_uri(self):
        return 'https://store.steampowered.com/search/?specials=1'
