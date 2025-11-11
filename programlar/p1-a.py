import math

a = math.cos(1.1)
b = math.sin(1.1)
z = a - (a / b) * b # Sifir olmasi gerekirken -5.551115123125783e-17 cikiyor.

print(z)