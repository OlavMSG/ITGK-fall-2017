def is_six_at_edge(list):
    if list[0] == 6 or list[-1] == 6:
        return True
    else:
        return False


def median(list):
    list1 = list
    list1.sort()
    midt = int(len(list)/2)
    if len(list) % 2 != 0:
        return list1[midt]
    else:
        return (list1[midt]+list1[midt+1])/2


def average(list):
    return sum(list)/len(list)


a = [6, 4, 3, 2, 1]
b = [1,3, 2]
c = [1, 2, 9, 4, 5, 6]

d = is_six_at_edge(a)
f = is_six_at_edge(b)
g = is_six_at_edge(c)
print(d, f, g)

h = average(a)
j = average(b)
l = average(c)
print(h, j , l)

x = median(a)
y = median(b)
z = median(c)
print(x, y, z)