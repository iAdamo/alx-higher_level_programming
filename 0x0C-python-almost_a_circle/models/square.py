#!/usr/bin/python3
"""
This is square module
It contains square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        strs = f"[{__class__.__name__}] ({self.id}) "
        strss = f"{self.x}/{self.y} - {self.width}"
        return strs + strss

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        # **kwargs must be skipped if *args exists and is not empty
        if len(args) > 0:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y 
            }
    