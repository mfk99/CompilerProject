from compiler.tokenizer import Token, tokenize

def test_tokenizer_simple() -> None:
    assert tokenize("if") == [Token(type='identifier', text='if')]

def test_tokenizer_basics() -> None:
    assert tokenize("if  3\nwhile") == [
        Token(type='identifier', text='if'), 
        Token(type='int_literal', text='3'), 
        Token(type='identifier', text='while')]

def test_tokenizer_single_operator() -> None:
    assert tokenize("==") == [
        Token(type='operator', text='==')]

def test_tokenizer_operators() -> None:
    assert tokenize("= == <= >") == [
        Token(type='operator', text='='), 
        Token(type='operator', text='=='), 
        Token(type='operator', text='<='), 
        Token(type='operator', text='>')]
    
def test_tokenizer_comment() -> None:
    assert tokenize("#if  3\nwhile") == [ 
        Token(type='identifier', text='while')]

''' 
def test_tokenizer_multiline_comment() -> None:
    assert tokenize("/* if  3\nwhile */ <") == [ 
        Token(type='operator', text='<')]
'''