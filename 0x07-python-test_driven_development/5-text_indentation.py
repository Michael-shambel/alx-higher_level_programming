#!/usr/bin/python3
"""this function going to check every text if any specified function showed it will print the line"""


def text_indentation(text):
    """
    this will print text after signes specification
    args:
    text: input text
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sign = ['.', '?', ':']
    lines = []
    l_count = ''

    for char in text:
        l_count += char
        if char in sign:
            lines.append(l_count.strip())
            l_count = ''

    if l_count:
        lines.append(l_count.strip())

    for i, line in enumerate(lines):
        print(line, end=' ' if i < len(lines) - 1 else '')
