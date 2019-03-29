class Dog():
    """representation of Dog class """
    def __init__(self):
        print('Dog created!')

    def Speaks(self):
        print('Dog says bark!')

    def Name(self):
        print("Dog's name is felix")


class Cat():
    """"representation of class cat"""
    def __init__(self):
        print('Cat created!')

    def Speaks(self):
        print("cat says meaow!")

    def Name(self):
        print("Cat's name isis")

class Bird():
    """representation of class birds"""
    def __init__(self):
        print('Birds created!')

    def Name(self):
        print('Birds name is sparrow')

    def Speaks(self):
        print('Bird speaks chicchi')

dog = Dog()
cat = Cat()
bird = Bird()

def func(obj):

    """ we can call the functions with the same name seperately rather
    than overriding just like Inheritance """
    obj.Name()
    obj.Speaks()

func(dog)
func(cat)
func(bird)
