# list is a collection of ordered, mutable elements; the type can be mixed (int, str, float, etc.)
# it's a data structure that allows to store multiple values inside a single variable
# use index to access items (start from 0)

myList = [1, 2, 3, 4, 5]
myList2 = list(("apple", "banana", "cherry"))

firstItem = myList[0]
print("First item in the list:", firstItem)

accessingLastItem = myList[-1]
print("Last item in the list:", accessingLastItem)

# slicing includes the start index and excludes the end index

accessingRange = myList[1:4]
print("Accessing range of items in the list:", accessingRange)

accessingEverySecondItem = myList[::2]
print("Accessing every second item in the list:", accessingEverySecondItem)

accessingReversedList = myList[::-1]
print("Accessing reversed list:", accessingReversedList)

accessingListLength = len(myList)
print("Length of the list:", accessingListLength)   

accessingListMaxValue = max(myList)
print("Max value in the list:", accessingListMaxValue)

accessingListMinValue = min(myList)
print("Min value in the list:", accessingListMinValue)

accessingListSum = sum(myList)
print("Sum of all items in the list:", accessingListSum)

accessingListAverage = sum(myList) / len(myList)
print("Average of all items in the list:", accessingListAverage)

accessingListCount = myList.count(3)
print("Count of item 3 in the list:", accessingListCount)

# 2 dimensional list (list of lists)
my2DList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("2D List:", my2DList)
print("Accessing item in 2D list:", my2DList[1][2])  # Accessing item 6 

# 3 dimensional list (list of lists of lists)
my3DList = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("3D List:", my3DList)
print("Accessing item in 3D list:", my3DList[1][0][1])  # Accessing item 6

# allowed operations on lists: append, insert, remove, pop, clear, index, count, sort, reverse, copy

myList[0] = 10  # changing the first item in the list
print("Modified list:", myList)

myList.append("apple")  # adding an item to the end of the list
print("List after appending 'apple':", myList)

myList.pop()
print("List after popping the last item:", myList)

myList.insert(3, 14)  # inserting an item at a specific index
print("List after inserting 14 at index 3:", myList)

myList.sort(); # warning! can't sort a list with mixed data types (int and str)
print("List after sorting:", myList)