# Exercise from Udemy course
# Practies the use of loops
# 1. simple looping from users input
count = input("How many times do I have to tell you?\n")
count = int(count)

for time in range(count):
    print(f"{time + 1}. CLEAN YOUR ROOM")
