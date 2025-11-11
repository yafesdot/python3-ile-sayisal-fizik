import math

def f(x):
    return math.exp(x)

def f1(x):
    return math.exp(x)

h = 0.1
x = 1.0

# Basliklar
print(f"{'h degeri':<15}{'Simet. Turev':<13}{'Tam Turev':<13}{'Sapma'}")

for i in range(12):
    f1_cd = (f(x + h) - f(x - h)) / (2 * h)
    f1_exact = f1(x)
    diff = f1_exact - f1_cd
    print(f"{h:.12f} {f1_cd:.10f} {f1_exact:.10f} {diff:.10f}")
    h = h / 10.0
