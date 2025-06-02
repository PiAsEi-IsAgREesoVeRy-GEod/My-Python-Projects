import random
import time
chatPassion = ["cooking","singing","dancing","music","culture and literacy"]
print("Welcome to Chatbot!")
name = input("What is your name? ")
print("Hello there",name, "It's a pleasure to meet you!")
food = input("What is something you're passionate about? ")
time.sleep(2)
print("That sounds lovely, I'm passionate about",random.choice(chatPassion))
day = input("Have you had a good day? ")
day = day.lower()
if day == 'yes':
    print("Good to hear that, me too")
else:
    print("Well I hope tomorrow is a better day for you")
print("Really enjoyed the chat, speak to you again soon.")
