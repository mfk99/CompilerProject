from typing import Literal
from dataclasses import dataclass
import re

TokentType = Literal["int_literal", 
                     "identifier", 
                     "parentheses", 
                     "operator", 
                     "comment",
                     "end"]

@dataclass(frozen=True)
class Token:
  type: TokentType
  text: str

def tokenize(source_code: str) -> list[str]:
  whitespace_re = re.compile(r'\s+')
  integer_re = re.compile(r'[0-9]')
  identifier_re = re.compile(r'[a-zA-Z0-9_]+')
  paren_re = re.compile(r'[()]')
  comment_re = re.compile(r'#.*\n|//')
  #multiline_comment_re = re.compile(r'/\*.*?\*/')
  #doesn't work for whatever reason
  #TODO fix
  operator_re = re.compile(r'==|=|!=|<=|>=|<|>|\+|-|\*|/')

  position = 0
  result: list[Token] = []

  while position < len(source_code):
    #nuh-uh bad solution, make it easier to add more shit
    match = whitespace_re.match(source_code, position)
    if match is not None:
      position = match.end()
      continue
      
    match = integer_re.match(source_code, position)
    if match is not None:
      result.append(Token(
        type='int_literal',
        text=source_code[position:match.end()]
      ))
      position = match.end()
      continue

    match = identifier_re.match(source_code, position)
    if match is not None:
      result.append(Token(
        type='identifier',
        text=source_code[position:match.end()]
      ))
      position = match.end()
      continue

    match = paren_re.match(source_code, position)
    if match is not None:
      result.append(Token(
        type='parentheses',
        text=source_code[position:match.end()]
      ))
      position = match.end()
      continue

    match = comment_re.match(source_code, position)
    if match is not None:
      position = match.end()
      continue
    
    '''
    match = multiline_comment_re.match(source_code, position)
    if match is not None:
      position = match.end()
      continue
    '''

    match = operator_re.match(source_code, position)
    if match is not None:
      result.append(Token(
        type='operator',
        text=source_code[position:match.end()]
      ))
      position = match.end()
      continue
    
    raise Exception(f'Tokenization failed near {source_code[position:(position + 10)]}...')

  # TODO cleanup
  return result