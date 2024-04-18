
import random
num = random.randint(1,10)
#print(num)

myChoice = input("Enter a number Between 1-10: ")
if num == myChoice:
  print(f"{num}, You have guessed the correct number")
else: 
  print(f"{num}, You have not guessed the correct number")
