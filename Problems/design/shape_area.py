from math import pi


class Shape:

    def area(self):
        print("Calculate area:")
        return 0

    def get_2decimal_digits(self, number):
        print("[Shape]->get_2decimal_digits: ")
        formatted_result = '{:0.2f}'.format(number)
        return formatted_result


class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        if side_a < 0 or side_b < 0:
            raise Exception("sides must be positive")
        self.a = side_a
        self.b = side_b

    def area(self):
        super().area()
        result = super().get_2decimal_digits(self.a * self.b)
        print("[Rectangle]->area: " + result)
        return result


class Circle(Shape):
    def __init__(self, _radius):
        if _radius < 0:
            raise Exception("radius must be positive")
        self.radius = _radius

    def area(self):
        super().area()
        result = super().get_2decimal_digits(pi * self.radius ** 2)
        print("[Circle]->area: "+result)
        return result


def test_case_1():
    circle = Circle(1)
    circle.area()
    rectangle = Rectangle(2,3)
    rectangle.area()


def test_case_2():
    circle = Circle(-5)
    circle.area()
    rectangle = Rectangle(-2,-3)
    rectangle.area()


def test_case_3():
    rectangle = Rectangle(-2,-3)
    rectangle.area()


def test():
    test_case_1()
    # test_case_2()
    # test_case_3()


test()
