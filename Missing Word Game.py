#Missing word game
import random
import time

options = ["There","their","They're"]
print("Welcome to the missing word game/n")
#Subprogram for question
def question():
    answer = input("\nWhich is the missing word?\nThere\ntheir\nThey're\n")
    return answer
#Question 1
question1 = "My parents bought ________ car yesterday."
print(question1)
answer = question()
if answer == options[1]:
    print("Excellent job, well done!")
else:
    print("Incorrect, let's try another one.")
time.sleep(3)
#Question 2
question2 = "\n_______ are no cookies left in the pink jar."
print(question2)
answer = question()
if answer == options[0]:
    print("Excellent job, well done!")
else:
    print("Incorrect, let's try another one.")
time.sleep(3)
#Question 3
print("\n_______ dancing by the sea shore.")
answer = question()
if answer == options[2]:
    print("Excellent job, well done!")
else:
    print("Incorrect, let's try another one.")
