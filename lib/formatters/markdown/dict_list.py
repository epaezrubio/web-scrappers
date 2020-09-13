from lib.formatters.base.base_formatter import BaseFormatter
from lib.utils.markdown import escape_markdown


class DictListMarkdownFormatter(BaseFormatter):
    def __init__(self):
        super(DictListMarkdownFormatter, self).__init__()

    def format(self, content, *args, **kwargs):
        msg = ''

        sorted_items = sorted(content.items(), key=lambda x: x[0], reverse=True)

        for key, value in sorted_items:
            msg = msg + "*{}:*\n".format(escape_markdown(key))

            for entry in value:
                msg = msg + "- {}\n".format(escape_markdown(entry))

            msg = msg + "\n"

        return msg
