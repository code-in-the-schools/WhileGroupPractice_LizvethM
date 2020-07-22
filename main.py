#random num
import random
num= random.randrange(-100,100)



found = False:

 while found == False:

   guess= int(import("Guess of a number between -100 and 100: "))
   if(guess>num):
     print(guess+" is more than it")
   elsif(guess<num):
     print(guess+"is less than it")
  else:
    print("You found it ")
