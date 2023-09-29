file1 = open("file.txt", "r")
file2 = open("file2.txt", "w")

lines = file1.readlines()
for line in lines:
    if line.startswith("T"):
        file2.write(line)
file1.close()
file2.close()
