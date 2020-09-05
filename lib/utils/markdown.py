import re

MARKDOWN_CHARACTERS = '*_`#'


def escape_markdown(text):
    escaped_text = text

    for char in MARKDOWN_CHARACTERS:
        escaped_text = escaped_text.replace(char, "\\{}".format(char))

    return escaped_text