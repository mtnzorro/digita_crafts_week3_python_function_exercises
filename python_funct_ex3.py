import math
import matplotlib.pyplot as plot

def f(x):
    return math.sqrt(x)

xs = range(-100, 101)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
