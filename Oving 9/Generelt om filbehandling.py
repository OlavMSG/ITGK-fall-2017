def write_to_file(data):
    f = open("my_file.txt", "w")
    f.write(data)
    f.close()

def read_from_file(filename):
    f = open(filename, "r")
    innhold = f.read()
    f.close()
    print(innhold)

def main():
    svar = "not done"
    print("Write 'done' to end the loop.")
    while svar != "done":
        svar = input("Do you want to read or write? ")
        if svar == "read":
            read_from_file("my_file.txt")
        elif svar == "write":
            data = input()
            write_to_file(data)
    print("You are done")


main()