from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    def __init__(self):
        super(BaseFormatter, self).__init__()

    @abstractmethod
    def format(self, content, *args, **kwargs):
        pass
