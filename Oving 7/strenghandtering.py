
def check_equal(str1, str2):
    if str1 == str2:
        return True
    else:
        return False


def reversed_word(str):
    str = list(str)
    list1 = [n for n in range(len(str))]
    for i in range(len(str)):
        list1[-i-1] = str[i]
    return "".join(list1)

def check_palindrome(str):
    if str == reversed_word(str):
        return True
    else:
        return False


def contains_string(str1, str2):
    for i in range(len(str1)):
        count = 0
        if str1[i] == str2[0]:
            for k in range(len(str2)):
                if str1[i+k] == str2[k]:
                    count += 1
            if count == len(str2):
                return i
    return -1


str1 = "hei"
str2 = "hello"
str3 = "hello"
print(check_equal(str1, str2))
print(check_equal(str3, str2))

str = "Morna Jens"
print(reversed_word(str))

str4 = "agnes i senga"
str5 = "hello"
print(check_palindrome(str4))
print(check_palindrome(str5))

str6 = "pepperkake"
str7 = "per"
str8 = "ola"
print(contains_string(str6, str7))
print(contains_string(str6, str8))