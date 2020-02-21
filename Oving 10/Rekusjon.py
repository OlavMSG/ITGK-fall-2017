from random import randint

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n-1)

def find_smallest_number_element(numbers):
    liste = numbers[:]
    Tmin = liste[1]
    Fmin = liste[0]
    if len(liste) == 2:
        if Tmin <= Fmin:
            return Tmin
        else:
            return Fmin
    else:
        if Tmin <= Fmin:
            liste = [Tmin]+liste[2:]
            return find_smallest_number_element(liste)
        else:
            liste = [Fmin]+liste[2:]
            return find_smallest_number_element(liste)


def binary_search(numbers, element):
    liste = numbers[:]
    imid = len(liste)//2
    if len(liste) == 2:
        if liste[0] == element:
            return 0
        elif liste[1] == element:
            return 1
        else:
            return -float('inf')
    elif liste[imid] == element:
        return imid
    elif element < liste[imid]:
        liste = liste[:imid]
        return binary_search(liste, element)
    elif element > liste[imid]:
        liste = liste[imid:]
        return imid + binary_search(liste, element)



print(recursive_sum(3))

numberlist = []
for i in range(10):
    numberlist.append(randint(1, 100))

print("numberlist: ", numberlist)
print("minste tall i numberlist er: ",find_smallest_number_element(numberlist))
numberlist.sort()
print(numberlist)
lett_etter = 19
print("leter etter: ", lett_etter)
print("element er i posisjon: ", binary_search(numberlist, lett_etter))
