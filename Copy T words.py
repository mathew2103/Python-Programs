file1 = open("file.txt", "r")
file2 = open("file2.txt", "w")

text = file1.readlines()
for line in text:
    words = line.split(' ')
    for word in words:
        if word.startswith("T") or word.startswith("t"):
            file2.write(word + "\n")
file1.close()
file2.close()
