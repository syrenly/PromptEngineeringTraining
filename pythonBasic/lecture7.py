# tuple collection of ordered, immutable elements
# use indexes to access items (start from 0)
myTuple = (1, 2, 3, 4, 5)

# single item tuple; comma at the end is mandatory to differentiate it from a regular parenthesis
singleItemTuple = (1,)

# accessing items in the tuple
thirdItem = myTuple[3]
print("Third item in the tuple:", thirdItem)

# negative indexing starts from the end of the tuple
print("Last item in the tuple:", myTuple[-1])

# tuple slicing includes the start index and excludes the end index
slicedTuple = myTuple[1:4]  
print("Sliced tuple (1:4):", slicedTuple)

# since tuple are immutable, we cannot change their values, but we can concatenate tuples to create a new one
newTuple = myTuple + (6, 7, 8)  
print("New tuple after concatenation:", newTuple)

print("Length of the tuple:", len(myTuple))

print("Max value in the tuple:", max(myTuple))

print("Min value in the tuple:", min(myTuple))

print("Sum of all items in the tuple:", sum(myTuple))

# counting occurrences of an item in the tuple
print("Count of item 3 in the tuple:", myTuple.count(3))

print("Index of item 4 in the tuple:", myTuple.index(4))