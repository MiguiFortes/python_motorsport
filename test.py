class Triangle:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def area(self):
        return 0.5 * self.__base * self.__altura

    
    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura



triangle = Triangle(10, 5)
print(triangle.area())