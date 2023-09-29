import random
x = int(input("Welcome to Dice Simulator.\nEnter number of random numbers to generate: "))
for i in range(x):    
    r = random.randint(1,6)
    print("Number generated:", r)
