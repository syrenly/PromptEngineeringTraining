# set is a collection of unordered and unique elements.
# Sets are mutable, meaning you can add or remove elements after the set has been created.
# no index present
numbers = {1, 2, 2, 3, 4, 3, 5}
print("Set of numbers (duplicates removed):", numbers)

# types of sets

data = {10, 20, 30}
fruits = {"apple", "banana", "cherry"}
values = {True, False}
mixedSet = {1, "apple", True, 3.14}
emptySet = set()  # to create an empty set, use the set() function
# if you use empty curly braces {}, it will create an empty dictionary, not a set.

fruits.add("orange")  # adding an item to the set
print("Fruits set after adding 'orange':", fruits)

fruits.remove("banana")  # removing an item from the set
print("Fruits set after removing 'banana':", fruits)

# union
a = {1, 2, 3}
b = {3, 4, 5}
c = a | b  # or a.union(b)
print("Union of sets a and b:", c)

# intersection
d = a & b  # or a.intersection(b)
print("Intersection of sets a and b:", d)

# for loop
for item in fruits:
    print("Fruit:", item)
