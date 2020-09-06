from lib.formatters.markdown.excerpt_list import ExcerptListFormatter


def test_excerpt_list():
    out = ExcerptListFormatter().format([
        ['foo', 'bar', 'test'],
        ['excerpt', 'list', 'test']])

    assert out == '*foo:*\n\nbar\ntest\n\n*excerpt:*\n\nlist\ntest\n\n'
