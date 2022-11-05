# Exercise from Udemy course
# Practies the use of loops
# 1. simple looping from users input
count = input("How many times do I have to tell you?\n")
count = int(count)

for time in range(count):
    print("CLEAN YOUR ROOM")
    if time >=3:
        print("do you even listen anymore?")
        break
