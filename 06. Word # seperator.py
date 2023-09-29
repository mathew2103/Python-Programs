f = open("file.txt", "r")
lines = f.readlines()
for line in lines:
    words = line.split()
    for word in words:
        print(word,end="#")
    print()
