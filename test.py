def validar_edad(edad):
    if edad <= 0:

        raise ValueError ("La edad no puede ser negativa")
    

try:
    validar_edad(-5)
except ValueError as e:
    print("Error inesperado:", e)
    print(e)    
