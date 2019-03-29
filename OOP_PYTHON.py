class MathsFunctions():

    """ contains various functions and algorithms of mathematics """
    global pi
    pi = 3.14

    def __init__(self):
        print('Class MathsFunctions created!')

    def CircleArea(self):
        """ returns the area of the circle"""
        radius = float(input('Enter the radius for Circle: '))
        return (pi * (radius ** 2))

    def CircleCircumference(self):
        """ returns the circumference of the circle """
        radius = float(input('Enter the radius of the circle: '))
        return (2 * pi * radius)

    def TriangleArea(self):
        """ returns the area of the triangle"""
        length = float(input('Enter the length of triangle: '))
        breath = float(input('Enter the breath of trianble: '))
        return (length * breath * 0.5)

    def SquareArea(self):
        """ return the Area of the square"""
        dimension = float(input('Enter the dimension of the square: '))
        return (dimension * dimension)

    def Slope(self):
        """ returns the slope or gradient """
        y1 = float(input('Enter y1: '))
        y2 = float(input('Enter y2: '))
        x1 = float(input('Enter  x1 :'))
        x2 = float(input('Enter x2: '))

        slope = (y2-y1) / (x2-x1)
        return slope


class Functions(MathsFunctions):
    """ calls all the functions of parent class 'MathsFunctions' """

    def __init__(self):
        print('Now you can call the fuctions from parent class')

    def SquareArea(self):
        print('The Area of the Square is 24 meter/square')


func = Functions()
