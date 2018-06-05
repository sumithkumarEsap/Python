import math
import random
number=random.randint(0,9)
print(number)
GuessedNum = int(input("enter the number between 0-9 :"))

while (number!=GuessedNum):
    if (GuessedNum < number):
        print("Your answer is low than required")
        GuessedNum = int(input("enter the number between 0-9 :"))


    elif (GuessedNum > number):
        print("Your answer is high than required")
        GuessedNum = int(input("enter the number between 0-9 :"))
else:
    print("congo")


