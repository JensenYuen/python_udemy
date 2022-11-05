# Exercise from Udemy course
# Practies the use of loops
# 3. printing emoji using both for and while loops

for num in range(1,11):
    print("\U0001f600"*num)

count = 0
while count < 11:
    print("\U0001f600"*count)
    count += 1
