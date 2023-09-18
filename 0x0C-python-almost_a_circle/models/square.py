#!/usr/bin/python3
"""
Square class
This module defines the Square class, a subclass of Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a Square, which is a subclass of Rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The x-position.
        y (int): The y-position.
        id (int): The unique identifier.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object with the provided attributes.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-position (default is 0).
            y (int, optional): The y-position (default is 0).
            id (int, optional): The unique identifier (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A formatted string representation of the object.
        """
        strs = f"[{__class__.__name__}] ({self.id}) "
        strss = f"{self.x}/{self.y} - {self.width}"
        return strs + strss

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is not greater than 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square object using either
        positional arguments (*args) or keyword arguments (**kwargs).

        Args:
            *args: Positional arguments to update attributes
            in the order: id, size, x, y.
            **kwargs: Keyword arguments to update attributes by name.
        """
        # **kwargs must be skipped if *args exists and is not empty
        if len(args) > 0:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square object.

        Returns:
            dict: A dictionary containing the attributes of the square.
        """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
