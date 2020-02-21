
def separate(numbers, threshold):
    list1 = []
    list2 = []
    for i in range(len(numbers)):
        if numbers[i] < threshold:
            list1.append(numbers[i])
        else:
            list2.append(numbers[i])
    return list1, list2


def multiplication_table(n):
    matrise = []
    for i in range(1, n+1):
        list = []
        for k in range(1, n+1):
            list.append(i*k)
        matrise.append(list)
    return matrise


numbers = [0, 9, 4, 5, 6, 2, 8, 3, 6, 4, 2]
print(separate(numbers, 5))

print(multiplication_table(4))