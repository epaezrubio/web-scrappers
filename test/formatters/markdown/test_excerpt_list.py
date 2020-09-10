from lib.formatters.markdown.excerpt_list import ExcerptListFormatter


def test_excerpt_list():
    out = ExcerptListFormatter().format([
        ['foo', 'bar', 'test'],
        ['excerpt', 'list', 'test']])

    assert out == '*foo:*\n\nbar\n\ntest\n\n\n*excerpt:*\n\nlist\n\ntest\n\n\n'
