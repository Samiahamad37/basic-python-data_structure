# x = 10
# def test():
#     y = 20
#     print(globals())  # Shows global namespace
#     print(locals())   # Shows local namespace
# test()


# def my_function():
#     y = 5  # 'y' is in the local namespace
#     print(y)
# my_function()

# print(y)  # Error! 'y' does not exist outside the function


# x = 42

# def my_function():
#     y = 10
#     print("Local Namespace:", locals())  # Shows local variables
#     print("Global Namespace:", globals())  # Shows global variables

# my_function()


# deleting tuple
# my_tuple = (1, 2, 3, 4)
# print(my_tuple)  # Output: (1, 2, 3, 4)

# Deleting the tuple
# del my_tuple


# tuple operation
# Defining tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
result = tuple1 + tuple2
print("Concatenation:", result)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
result = tuple1 * 2
print("Repetition:", result)  # Output: (1, 2, 3, 1, 2, 3)

# Membership
print(2 in tuple1)  # Output: True
print(4 not in tuple1)  # Output: True

# Length
print("Length:", len(tuple1))  # Output: 3


my_tuple = (10, 20, 30, 40)
my_list = [10, 20, 30, 40]

# Access elements by index
print(my_tuple[0])  # Output: 10
print(my_list[1])   # Output: 20

# Negative indexing
print(my_tuple[-1])  # Output: 40
print(my_list[-2])   # Output: 30



my_tuple = (10, 20, 30, 40, 50)
my_list = [10, 20, 30, 40, 50]

# Slicing: [start:end:step]
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_list[::2])   # Output: [10, 30, 50]

# Negative slicing
print(my_tuple[-4:-1])  # Output: (20, 30, 40)
print(my_list[::-1])    # Output: [50, 40, 30, 20, 10]





# List matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(matrix[1][2])  # Output: 6 (2nd row, 3rd column)

# Tuple-like structure matrix
tuple_matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tuple_matrix[0][1])  # Output: 2 (1st row, 2nd column)
