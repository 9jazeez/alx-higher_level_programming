#!/usr/bin/python3


"""A module that contains a class that inherits from
Python's main list class.


"""

class MyList(list):
    """ A cclass with the proerties of list class
    from  python main list object

    """

    def __init__(self):
        """The init function also takes from the main
        pareent class list

        Args
        self

        """
        super().__init__()

    def print_sorted(self):
        """ A mehod that that returns the sorted list of
         a given list. Also inherted

        """

        self.copy = self[:]
        self.copy.sort()
        print(self.copy)
