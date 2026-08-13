# function is a piece of code that can be reused multiple times in a program.
def greet(): # indentation is required for the function body
    print("Hello from my function!")

greet()  # calling the function to execute its code

# functions with parameters allow you to pass data into the function for processing.
def greet_person(name):  # 'name' is a parameter
    print(f"Hello, {name}!")  # using the parameter in the function body    

greet_person("Alice")  # calling the function with an argument

# functions with return value

def add_numbers(a, b):  # function with two parameters
    return a + b  # returning the sum of the two parameters 

add_result = add_numbers(5, 3)  # calling the function and storing the result
print("Sum of 5 and 3 is:", add_result)  # printing the result

# functions with default parameters allow you to specify default values for parameters if no argument is provided during the function call.
def greet_with_default(name="Guest"):  # 'name' has a default value of "Guest"
    print(f"Hello, {name}!")  # using the parameter in the function body

greet_with_default()  # calling the function without an argument, will use the default value    
greet_with_default("Bob")  # calling the function with an argument, will override the default value