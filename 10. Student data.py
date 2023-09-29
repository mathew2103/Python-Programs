import pickle

def add():
    f = open("students.dat", "ab")
    name = input("Enter name:")
    rollNo = int(input("Enter roll no:"))
    marks = int(input("Enter marks:"))
    x = {"Name": name, "rNo": rollNo, "Marks": marks}
    pickle.dump(x, f)
    f.close()

def display():
    f = open("students.dat", "rb")
    try:
        while True:
            p = pickle.load(f)
            print(p)
    except EOFError:
        f.close()

def update():
    f = open("students.dat", "rb")
    rNo = int(input("Enter roll no:"))
    marks = int(input("Enter new marks: "))
    lst = []
    try:
        while True:
            p = pickle.load(f)
            lst.append(p)
    except EOFError:
        f.close()
        
    for i in range(len(lst)):
        if lst[i]["rNo"] == rNo:
            lst[i]["Marks"] = marks
    f = open('students.dat', 'wb')
    for i in lst:
        pickle.dump(i,f)

while True:
    o = int(input("Menu:\n1. Add new record\n2. Update record\
    \n3. Display records\n4. Exit\nChoose your option: "))
    if o == 1:
        add()
    elif o == 2:
        update()
    elif o == 3:
        display()
    elif o == 4:
        print("Exiting")
        break
    else:
        print("Invalid input")

