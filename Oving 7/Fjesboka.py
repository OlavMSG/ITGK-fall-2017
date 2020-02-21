
def add_data(user_data):
    user_data_list = user_data.split(" ")
    user_data_list[2] = int(user_data_list[2])
    facebook.append(user_data_list)


def get_person(given_name, facebook):
    list = []
    for i in range(len(facebook)):
        if given_name == facebook[i][0]:
            list.append(facebook[i])
    return list


def main():
    print("Hello, welcome to Facebook. Add a new "
          "user by writing 'given_name surname "
          "age gender relationship_status'")
    print("Answer 'done' when done")
    new_user_data = "not done"
    while new_user_data != "done":
        new_user_data = input("Add a new user: ")
        if new_user_data != "done":
            add_data(new_user_data)
    print("Ok")
    given_name = "not done"
    while given_name != "done":
        given_name = input("Search for a user: ")
        list = get_person(given_name, facebook)
        if list == []:
            print(list)
        else:
            print(list[0][0], list[0][1], "is", list[0][2],
                  "years old, his relationship status is",
                  list[0][4])



facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"],
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"]]

print(add_data("Mark Zuckerberg 32 Male Married"))
print(get_person("Mark", facebook))
main()

