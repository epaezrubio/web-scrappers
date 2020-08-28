from lib.formatters.markdown.dict_list import DictListMarkdownFormatter


def test_dict_list():
    d = { 'foo': ['bar', 'test'] }
    out = DictListMarkdownFormatter().format(d)

    assert out == '*foo:*\n- bar\n- test\n\n'


def test_multi_dict_list():
    d = { 'foo': ['bar', 'test'], 'lmao': ['one', 'two'] }
    out = DictListMarkdownFormatter().format(d)

    assert out == '*foo:*\n- bar\n- test\n\n*lmao:*\n- one\n- two\n\n'
