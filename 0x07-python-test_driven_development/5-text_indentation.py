#!/usr/bin/python3

"""This module contain a function that helps print
blank lines

"""


def text_indentation(text):
    """Test indentation function
    Spaces the string at ., ?, :

    Args:
    str (text): String to spaced

    """
    try:
        if not isinstance(text, str):
            raise TypeError('text must be a string')
        elif text is None:
            pass
        else:
            for i in text:
                print(i, end="")
                if i in (".", "?", ":"):
                    print()
                    print()
    except Exception as err:
        print(err)
