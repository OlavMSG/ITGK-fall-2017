def gcd(a, b):
    while b != 0:
        gammel_b = b
        b = a%b
        a = gammel_b
    return a


def reduce_fraction(a, b):
    d = gcd(a, b)
    return int(a/d), int(b/d)

a = int(input("Et heltall, a= "))
b = int(input("Et heltall, b = "))

var_a, var_b = reduce_fraction(a, b)
print(a, "/", b, "kan forkortes til", var_a, "/", var_b)