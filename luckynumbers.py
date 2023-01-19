# Exercise from Udemy course
# Practies the use of loops
# 2. loop though number 1-20
# if 4 & 13, print unlucky
# if even number, print even
# if odd number, print odd

for num in range(1,21):
    if num == 4 or num == 13:
        print(f"num {num} is unlucky")
    elif num % 2 == 0:
        print(f"num {num} is even")
    else:
        print(f"num {num} is odd")
