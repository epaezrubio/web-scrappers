from lib.formatters.base.base_formatter import BaseFormatter
from lib.utils.markdown import escape_markdown


class ExcerptFormatter(BaseFormatter):
    def __init__(self):
        super(ExcerptFormatter, self).__init__()

    def format(self, content, *args, **kwargs):
        if content[1]:
            string = '*{}:*\n\n{}\n{}'
        else:
            string = '*{}:*{}\n\n{}\n'

        return string.format(escape_markdown(content[0]),
            escape_markdown(content[1]), escape_markdown(content[2]))
