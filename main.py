import random
import time

hidden_num = random.randint(1, 100)
tries = 7
user = int(input("Enter a number from 1 to 100: "))

if user > 100 or user < 0:
    print("Error, pls try enter another number from 1 to 100 only")
    user = int(input("Enter a number: "))

while (user != hidden_num and user <= 100 and user >= 1) and tries > 0:
    if user > hidden_num:
        print("Too high")
        print(f"You have {tries} tries left")
        tries -= 1
        user = int(input("Enter a number: "))
    elif user < hidden_num:
        print("Too low")
        print(f"You have {tries} tries left")
        tries -= 1
        user = int(input("Enter a number: "))
    else:
        break
if user == hidden_num:
    if tries == 1:
        print("Congrats, you win with 1 try left.")
    else:
        print(f"Congrats, you win with {tries} tries left.")
else:
    print("You lose. The number was {}".format(hidden_num))

time.sleep(6)
