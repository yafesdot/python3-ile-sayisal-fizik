import numpy as np
import matplotlib.pyplot as plt

def f(x, v, t):
    """Tek boyutta olduğundan adi hareket denklemi"""
    return -x

n = 200
h = 6.28 / n
t = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)

# Baslangic kosullari
t[0] = 0.0
x[0] = 0.0
v[0] = 1.0

for i in range(1, n):
    t[i] = h * i
    x[i] = x[i-1] + v[i-1] * h
    v[i] = v[i-1] + f(x[i-1], v[i-1], t[i-1]) * h
    print(f"{t[i]:.12f} {x[i]:.10f} {v[i]:.10f}")

plt.plot(t, x, label='X(t) (Konum)')
plt.plot(t, v, label='V(t) (Hız)')
plt.xlabel('Zaman (t)')
plt.ylabel('Konum (X) ve Hız (V)')
plt.legend()
plt.title('Bir Boyutta Hareket')
plt.grid(True)
plt.show()
