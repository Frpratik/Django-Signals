class Rectangle:
    """
    Rectangle class:
    - Takes length and width.
    - Is iterable.
    - When you loop over it, you first get {'length': value} then {'width': value}.
    """

    def __init__(self, length: int, width: int):
        # Stores the given length and width in the object
        self.length = length
        self.width = width

    def __iter__(self):
        """
        This makes the Rectangle iterable.
        'yield' returns one item at a time.
        The loop using this object will get:
          1. {'length': value}
          2. {'width': value}
        """
        yield {'length': self.length}
        yield {'width': self.width}

# ex.
rect = Rectangle(8, 2)

for value in rect:
    print(value)

# o/p:
# {'length': 8}
# {'width': 2}
