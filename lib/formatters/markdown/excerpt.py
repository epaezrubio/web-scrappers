from lib.formatters.base.base_formatter import BaseFormatter
from lib.utils.markdown import escape_markdown


class ExcerptFormatter(BaseFormatter):
    def __init__(self):
        super(ExcerptFormatter, self).__init__()

    def format(self, content, *args, **kwargs):
        return '*{}:*\n\n{}\n{}'.format(escape_markdown(content[0]),
            escape_markdown(content[1]), escape_markdown(content[2]))
