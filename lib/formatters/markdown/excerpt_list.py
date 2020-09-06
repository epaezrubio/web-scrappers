from lib.formatters.markdown.excerpt import ExcerptFormatter

class ExcerptListFormatter(ExcerptFormatter):
    def __init__(self):
        super(ExcerptFormatter, self).__init__()

    def format(self, content, *args, **kwargs):
        string = ''

        for c in content:
            string += '{}\n\n'.format(
                super(ExcerptListFormatter, self).format(c, *args, **kwargs))

        return string
