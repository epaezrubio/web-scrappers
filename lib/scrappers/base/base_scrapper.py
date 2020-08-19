from abc import ABC, abstractmethod


class BaseScrapper(ABC):
    def __init__(self):
        super(BaseScrapper, self).__init__()

    @abstractmethod
    def scrap(self, *args, **kwargs):
        pass
