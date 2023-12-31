# -*- coding: utf-8 -*-
"""Ejercicio 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_1MhLFE2N-bPXqr0Km7JPfXAaSVqwKsz
"""

# areaCirculo: num -> num
# calcula el area de un circulo de medidas
# r
# ademas se debe considerar pi = 3.14
# ejemplo areaCirculo(3) debe producir 28.26
def areaCirculo(r):
  pi=3.14
  return pi*r**2

#Tests
assert areaCirculo(3)==28.26

# areaAnillo: num num -> num
# calcula el area de un anillo de medidas
# r_exterior y r_interior
# ejemplo areaAnillo(5,3) debe producir 50.239999999999995
def areaAnillo(r_exterior,r_interior):
    return areaCirculo(r_exterior)-areaCirculo(r_interior)

#Test
assert areaAnillo(5, 3)==50.239999999999995

# perimetroCirculo: num -> num
# calcula el perimetro de un circulo de medidas
# r
# ademas se debe considerar pi = 3.14
# ejemplo perimetroCirculo(3) debe producir 18.84
def perimetroCirculo(r):
  pi=3.14
  return 2*r*pi

#Tests
assert perimetroCirculo(3)==18.84

# perimetroAnillo: num num -> num
# calcula el perimetro de un anillo de medidas
# r_exterior y r_interior
# ejemplo perimetroAnillo(5,3) debe producir 50.24
def perimetroAnillo(r_exterior,r_interior):
    return perimetroCirculo(r_exterior)+perimetroCirculo(r_interior)

#Test
assert perimetroAnillo(5, 3)==50.24