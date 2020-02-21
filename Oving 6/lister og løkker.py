def lag_number_list():
    number_list = []
    for i in range(100):
        number_list.append(i)
    return number_list


def summer_delig_3_og_10(number_list):
    sum = 0
    for j in number_list:
        if (j%3 == 0) or (j%10 == 0):
            sum += j
    print("sum =", sum)

def bytterplass(number_list):
    for k in range(0, 100, 2):
        plassholder = number_list[k]
        number_list[k] = number_list[k+1]
        number_list[k+1] = plassholder
    print(number_list)

def revers_list(number_list):
    reversed_list = []
    for x in range(1, 100, 1):
        list1 = [number_list[-x]]
        reversed_list = reversed_list + list1
    reversed_list = reversed_list + [number_list[0]]
    print(reversed_list)



number_list = lag_number_list()
print(number_list)

summer_delig_3_og_10(number_list)
bytterplass(number_list)
revers_list(number_list)
