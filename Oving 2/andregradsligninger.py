print("Skriv inn en verdi for a, b og c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2-4*a*c

if d < 0:
    print("Andregradsligningen ",a,"*x^2+",b,"x+",c,"har to imaginære løsninger")
elif d > 0:
    print("Andregradsligningen ", a, "*x^2+", b, "x+", c, "har to reelle løsninger")
else:
    print("Andregradsligningen ", a, "*x^2+", b, "x+", c, "har én reell dobbelrot")