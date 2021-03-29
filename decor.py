from matplotlib.pyplot import plot, show
import numpy as np
def fun1(f):
    a = np.linspace(1,10,100)
    b = f(a)
    plot(b,a)
    show()

    
@fun1
def sen(x):
    return np.sin(x)

print(sen(np.pi))
