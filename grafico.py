import matplotlib.pyplot as plt
import numpy as np

f = lambda x: 2*x + 1

t = np.linspace( 0, 10, 100)
y = list(map(f, t))

plt.plot(t, y)
plt.title("Grafiquinho")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()


