#!/usr/bin/python3


"""
This module containss a rectangle class that
inherits from the base class

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square with width.
    Also inherits from class Rectangle

    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def area(self):
        """Returns area"""
        ar = self.width * self.height
        return (ar)

    def display(self):
        """Display method"""
        for i in range(self.x):
            print()
        for i in range(self.height):
            print("{} {}".format(" " * self.y, "#" * self.width))

    def __str__(self):
        """Overriding the __str__"""
        id_str = " (" + str(self.id) + ")"
        a = " " + str(self.x) + "/"
        b = str(self.y) + " "
        c = str(self.width)

        return ("[Square]" + id_str + a + b + "- " + c)

    @property
    def size(self):
        """Getter"""
        return (self.width)

    @size.setter
    def size(self, size):
        """Setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Method to update all attr"""
        if args:
            myattr = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, myattr[i], e)
            return
        for x, y in kwargs.items():
            if hasattr(self, x):
                setattr(self, x, y)

    def to_dictionary(self):
        """Dictionary"""
        Dict = {}
        for x, y in vars(self).items():
            if x.startswith("_"):
                if not x.endswith("width") and not x.endswith("height"):
                    idx = x.index("__")
                    Dict[x[idx + 2:]] = y
                else:
                    Dict["size"] = y
            else:
                Dict[x] = y
        return (Dict)
