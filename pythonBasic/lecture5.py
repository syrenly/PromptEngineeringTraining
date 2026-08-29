# break statement (exits the loop when a condition is met)

for i in range(1, 6):
    if i == 3:
        print("Found 3, breaking the loop.")
        break
    print("Current number in loop:", i)

# continue statement (skips the current iteration and continues with the next one)

for i in range(1, 6):
    if i == 3:
        print("Skip step 3")
        continue
    print("Current number in loop:", i)
