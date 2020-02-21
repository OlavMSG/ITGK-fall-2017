from math import *


def f(x):
    return (x-12)*exp(5*x)-8*(x+2)**2


def g(x):
    return -x-2*x**2-5*x**3+6*x**4


def deriverte(h, x, func):
    return (func(x+h/2)-func(x-h/2))/h



def newtons_method(h, x, func, tol):
    while True:
        if abs(-(func(x)/deriverte(h, x, func))) >= tol:
            x = x -(func(x)/deriverte(h, x, func))
        else:
            x = x - (func(x) / deriverte(h, x, func))
            break
    return x


a = newtons_method(0.00000001, -2, f, 0.0000000001)
b = newtons_method(0.00000001, 1, g, 0.0000000001)
c = newtons_method(0.00001, -1, g, 0.00001)

print("Funksjonen nærmer seg et nullpunkt når x =", a, "da er y =", f(a))
print("Funksjonen nærmer seg et nullpunkt når x =", b, "da er y =", g(b))
print("Funksjonen nærmer seg et nullpunkt når x =", c, "da er y =", f(c))







