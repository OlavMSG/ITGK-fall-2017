def add_family_member(role, name):
    if role in my_family:
        list = [my_family[role]]
        list.append(name)
        name = list
    my_family[role] = name


my_family ={}
add_family_member("bror", "Arne")
add_family_member("mor", "Anne")
add_family_member("bror", "Geir")
print(my_family)
