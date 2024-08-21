from sys import argv
from datetime import datetime
from os.path import basename, exists, isdir
from os import listdir


def formatter(line):
    return "** " + line
def injector(_path):
    lines = []
    topLine = "/"
    for x in range(30):
        topLine += "*"

    if not exists(_path):
        print("Path does not exist!!")
        exit()

    info = []
    info.append(basename(_path))
    info.append(input("Project: "))
    info.append(input("Author: "))
    date = input("Date (enter nothing and the current date will be used): ")

    if not date:
        date = str(datetime.now())
        date = date.split('-')
        date = date[1] + '/' + date[2].split(" ")[0] + '/' + date[0]
    info.append(date)

    section = input("Section: ")
    info.append(section)

    email = input("Email: ")
    info.append(email)

    line = 0
    count = 1
    description = []
    while line != 'end':
        line = input(str(count) + ": ")
        count += 1
        if line != 'end':
            description.append(line)
    info.append(description)

    categories = ("File", "Project", "Author", "Date", "Section", "E-mail")

    lines.append(topLine)
    for cat in categories:
        add = 9 - len(cat)
        new = ""
        for i in range(add):
            new += " "
        lines.append("** " + cat + ":" + new + info[categories.index(cat)])

    lines.append("**")
    for lin in description:
        lines.append("** " + lin)

    lines.append("**")
    lines.append("**")
    lines.append(topLine[1:] + topLine[0])

    print("--Your Header--")
    for j in lines:
        print(j)

    yn = 'o'
    while yn != 'y' and yn != 'n':
        yn = input("Inject into file(y/n)? ")
    if yn == 'y':
        for i in range(len(lines)):
            lines[i] += '\n'
        with open(_path, 'r') as op:
            _file = op.readlines()
        with open(_path, 'w') as op:
            lines.append('\n')
            op.writelines(lines)
            op.writelines(_file)
        print("Injected!")
    else:
        print("Not injected!")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Error! Submit a file path!")
    elif argv[1].endswith("*.cpp"):
        directory = argv[1].split("\\*.cpp")[0]
        if isdir(directory):
            for x in [y for y in listdir(directory) if y.endswith(".cpp")]:
                print("File: " + x)
                injector(directory + "\\" + x)
        else:
            print("Invalid Directory")
    else:
        injector(argv[1])
