from abc import ABC, abstractmethod


class BaseOutput(ABC):
    def __init__(self):
        super(BaseOutput, self).__init__()

    @abstractmethod
    def output(self, content, *args, **kwargs):
        pass
