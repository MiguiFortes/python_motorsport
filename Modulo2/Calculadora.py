class calculadora:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def suma(self):
        return self.a + self.b
  

    def resta(self):
        return self.a - self.b
    

calc = calculadora(5,5)
print(calc.suma())

calc=calculadora (10,5)
print(calc.suma())