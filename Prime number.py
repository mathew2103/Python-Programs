x = int(input("Enter number: "))

for i in range(2,x//2):
    if x%i == 0:
        print(x,"is not prime.")
        break
else:
    print(x,"is prime.")
