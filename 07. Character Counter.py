file = open("file.txt", "r")
content = file.read()

vCount = 0
cCount = 0
uCount = 0
lCount = 0

for letter in content:
    if letter.isalpha():
        if letter.lower() in ['a','e','i','o','u']:
            vCount += 1
        else:
            cCount += 1

        if letter.islower():
            lCount += 1
        else:
            uCount += 1

print("Number of vowels:",vCount)
print("Number of consonants:",cCount)
print("Number of lowercase characters:",lCount)
print("Number of uppercase characters:",uCount)
