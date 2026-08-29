# function arguments are the actual values that are passed to the function when it is called.
# parameters are placeholders for the values that will be passed to the function when it is called.
def multiply_numbers(x, y):  # function with two parameters
    return x * y  # returning the product of the two parameters


result = multiply_numbers(4, 5)  # calling the function with arguments
print("Product of 4 and 5 is:", result)  # printing the result

# lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions.
square = lambda x: x**2  # lambda function to calculate the square of a number
print("Square of 6 is:", square(6))  # calling the lambda function with an argument


def square_number(num):  # function to calculate the square of a number
    return num**2  # returning the square of the number


print("Square of 7 is:", square_number(7))  # calling the function with an argument

# lambda functions are used when we have short logic, one time use and when we want to use a function inside another function.
# they are often used in higher-order functions like map(), filter(), and reduce() where we need to pass a function as an argument.


def filter_even_numbers(numbers):  # function to filter even numbers from a list
    return list(
        filter(lambda x: x % 2 == 0, numbers)
    )  # using a lambda function to filter even numbers, using list() to convert the filter object to a list


even_numbers = filter_even_numbers(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
)  # calling the function with a list of numbers
print("Even numbers in the list are:", even_numbers)


def map_square_numbers(numbers):  # function to map square of numbers from a list
    return list(
        map(lambda x: x**2, numbers)
    )  # using a lambda function to calculate the square of each number, using list() to convert the map object to a list


squared_numbers = map_square_numbers(
    [1, 2, 3, 4, 5]
)  # calling the function with a list of numbers
print("Squared numbers in the list are:", squared_numbers)
