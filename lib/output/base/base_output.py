from abc import ABC


class BaseOutput(ABC):
    def __init__(self):
        super(BaseOutput, self).__init__()

    @abstractmethod
    def output(self, *args, **kwargs):
        pass
