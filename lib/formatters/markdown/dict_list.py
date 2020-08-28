from lib.formatters.base.base_formatter import BaseFormatter


class DictListMarkdownFormatter(BaseFormatter):
    def __init__(self):
        super(DictListMarkdownFormatter, self).__init__()

    def format(self, content, *args, **kwargs):
        msg = ''

        for key, value in content.items():
            msg = msg + "*{}:*\n".format(key)

            for entry in value:
                msg = msg + "- {}\n".format(entry)

            msg = msg + "\n"

        return msg
