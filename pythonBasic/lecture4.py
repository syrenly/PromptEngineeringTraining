# range function => creates a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# range(start, stop, step)

myRange = range(1, 6)
print("Range from 1 to 5:", list(myRange))

# for loop
for i in range(1, 6):
    print("Current number:", i)

# while loop (runs until a condition is met)

count = 1

while count <= 5:
    print("Count is:", count)
    count += 1
