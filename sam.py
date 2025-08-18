# x={
#     "color":"green",
#     "shoes":"4angle",
#     "clothes":"gown",
# }
# for x in y:
# print(y[x])

# List matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(matrix[1][2])  # Output: 6 (2nd row, 3rd column)

# Tuple-like structure matrix
tuple_matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tuple_matrix[0][1])  # Output: 2 (1st row, 2nd column)





my_tuple = (10, 20, 30, 10, 40)

# 1. `len()`: Get the length of the tuple
print(len(my_tuple))  # Output: 5

# 2. `max()`: Find the maximum value
print(max(my_tuple))  # Output: 40

# 3. `min()`: Find the minimum value
print(min(my_tuple))  # Output: 10

# 4. `sum()`: Sum all elements
print(sum(my_tuple))  # Output: 110

# 5. `count()`: Count the occurrences of a value
print(my_tuple.count(10))  # Output: 2

# 6. `index()`: Find the index of the first occurrence of a value
print(my_tuple.index(30))  # Output: 2

# 7. `tuple()`: Convert another data type to a tuple
my_list = [1, 2, 3]
print(tuple(my_list))  # Output: (1, 2, 3)



