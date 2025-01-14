#Rectangle class :

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

if __name__ == "__main__":
    rect = Rectangle(length=10, width=5)

    for dimension in rect:
        print(dimension)
