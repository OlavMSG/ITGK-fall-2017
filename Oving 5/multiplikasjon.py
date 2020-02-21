def multi(tol):
    prod = 1
    count = 0
    i = 1
    while True:
        if (prod*(1+1/(i**2)) - prod) >= tol:
            prod *= (1+1/(i**2))
            i += 1
            count += 1
        else:
            prod *= (1 + 1 / (i ** 2))
            count += 1
            break
    return round(prod, 2), count

tol = float(input("# tol = "))

prod, count = multi(tol)
print("Produktet ble", prod, "etter", count, "iterasjoner.")
