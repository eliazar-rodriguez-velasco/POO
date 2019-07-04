class Operations:
 def __init__(self):
  pass
 def area_cuadrado(self,number1,number2):
  return number1*number2

 def perimetro_cuadrado(self,number1):
  return (number1)*4 

 def area_triangulo(self,number1,number2):
  return number1*number2/2

 def perimetro_triangulo(self,lado1,lado2,base3):
  return lado1+lado2+base3

 def area_trapecio(self,base1,base2,haltura3):
  return (base1+base2)*haltura3/2

 def perimetro_trapecio(self,base_menor1,base_mayor2,lado1,lado2):
  return base_menor1+base_mayor2+lado1+lado2

 def area_circulo(self,radio1):
  return 3.1416*(radio1**2)

 def perimetro_circulo(self,radio2):
  return 3.1416*(radio2)

object = Operations()
print("area_cuadrado",object.area_cuadrado(8,3))

print("area_triangulo",object.area_triangulo(7,4))

print("area_trapecio",object.area_trapecio(6,8,4))

print("area_circulo",object.area_circulo(6))

print("perimetro_cuadrado",object.perimetro_cuadrado(5))

print("perimetro_triangulo",object.perimetro_triangulo(3,5,6))

print("perimetro_trapecio",object.perimetro_trapecio(5,5,4,7))

print("perimetro_circulo",object.perimetro_circulo(6))





