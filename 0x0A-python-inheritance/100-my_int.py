#!/usr/bin/python3


"""This module contains a class that inherits from
python's int class.
"""


class MyInt(int):
    """An int class that inherits from python's
    main int and inverts it eq and ne
    """

    def __init__(self):
        """Inherits from the class int

        Args:
        self

        """
        super().__init__()

    def __ne__(self, other):
        """Compares an instance with other using
        negation

        Args
        other (other): argument to compare with
        """

        return super().__eq__(other)

    def __eq__(self, other):
        """Compares an instance with other using
        equality

        Args
        other (other): argument to compare with
        """

        return super().__ne__(other)
