import csv

file = open("sports.csv", "w")
writer = csv.writer(file, delimiter="\t")
writer.writerow(["Sport", "Competitions", "Prizes Won"])
x = int(input("Enter number of entries: "))
for i in range(x):
    print(f"Record {i+1}/{x}")
    spName = input("Enter Sport Name: ")
    compCount = int(input("Enter number of competitions: "))
    prizeCount = int(input("Enter prize count: "))
    l = [spName, compCount, prizeCount]
    writer.writerow(l)
    print("Record added")
file.close()
