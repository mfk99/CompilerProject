from compiler.tokenizer import tokenize

def test_tokenizer_basics():
    assert tokenize("if  3\nwhile") == ['if', '3', 'while']