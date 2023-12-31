import pickle
f = open("students.dat", 'ab')

def add():
    name = input("Enter name:")
    rollNo = int(input("Enter roll no:"))
    marks = int(input("Enter marks:"))
    x = {"Name": name, "rNo": rollNo, "Marks": marks}
    pickle.dump(x, f)
    f.close()
    print("Added new record")

def find():
    f = open("students.dat", "rb")
    rollNo = int(input("Enter roll no:"))
    try:
        while True:
            p = pickle.load(f)
            if p["rNo"] == rollNo:
                print(p)
                break
    except EOFError:
        print("No record found")
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
    o = int(input("Menu:\n1. Add new record\n2. Search record\
    \n3. Display records\n4. Update Record\n5. Exit\nEnter required option: "))
    if o == 1:
        add()
    elif o == 2:
        find()
    elif o == 3:
        display()
    elif o == 4:
        update()
    elif o == 5:
        print("Exiting")
        break
    else:
        print("Invalid input")
