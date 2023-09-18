#!/usr/bin/python3
"""
rectangle module
Supplies the Rectangle class: A subclass of Base class.
"""
from models.base import Base


class Rectangle(Base):
    """
    This class represents a Rectangle, which is a subclass of the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-position of the rectangle.
        y (int): The y-position of the rectangle.
        id (int): The unique identifier of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object with the provided attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-position of the rectangle (default is 0).
            y (int, optional): The y-position of the rectangle (default is 0).
            id (int, optional): The unique identifier of the
            rectangle (default is None).
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle using '#' characters,
        considering its position (x, y).
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A formatted string representation of the object.
        """
        strs = f"[{__class__.__name__}] ({self.id}) "
        strss = f"{self.x}/{self.y} - {self.width}/{self.height}"
        return strs + strss

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle object using either
        positional arguments (*args) or keyword arguments (**kwargs).

        Args:
            *args: Positional arguments to update attributes in the order:
            id, width, height, x, y.
            **kwargs: Keyword arguments to update attributes by name.
        """
        # **kwargs must be skipped if *args exists and is not empty
        if len(args) > 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle object.

        Returns:
            dict: A dictionary containing the attributes of the rectangle.
        """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x-position attribute.

        Returns:
            int: The x-position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x-position attribute.

        Args:
            value (int): The x-position to set.

        Raises:
            TypeError: If the x-position is not an integer.
            ValueError: If the x-position is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y-position attribute.

        Returns:
            int: The y-position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-position attribute.

        Args:
            value (int): The y-position to set.

        Raises:
            TypeError: If the y-position is not an integer.
            ValueError: If the y-position is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
