from lib.output.base.base_output import BaseOutput


class ConsoleOutput(BaseOutput):
    def __init__(self):
        super(ConsoleOutput, self).__init__()

    def output(self, content, *args, **kwargs):
        print(content)