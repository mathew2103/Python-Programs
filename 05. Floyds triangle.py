n = int(input("Enter number of rows: "))
x = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(x, end=" ")
        x+=1
    print()
