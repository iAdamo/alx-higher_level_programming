#!/usr/bin/python3
"""Text indentation module

Test file for this module is located in ./tests/ directory
Run (python3 -m doctest -v ./tests/5-text_indentation.txt | tail -2)
to test remove the pipeline to see full details"""


def text_indentation(text):
    """text_indentation - prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text:must be a string

    Return:
        Nothing
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    _text = text.replace('.', '\n\n').replace('?', '\n\n').replace(':', '\n\n')
    for _ in range(len(text)):
        _text = _text.replace('\n ', '\n')
    print(_text, end='')
