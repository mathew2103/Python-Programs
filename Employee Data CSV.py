import csv


def writeData():
    file = open("record.csv", "a")
    writer = csv.writer(file)
    empId = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    mobile = int(input("Enter mobile number: "))
    l = [empId, name, mobile]

    writer.writerow(l)
    print("Added record")


def countR():
    file = open("record.csv", "r")
    reader = csv.reader(file)
    x = 0
    for i in reader:
        if len(i):
            x += 1
    print("Number of records:", x)


writeData()
countR()
