# Q2: Student Marks Analysis (no loops or functions used)

# 1. Create a list of five marks and convert it into a tuple
marks_list = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks_list)

# 2. Display both collections and their data types
print("Marks (list):", marks_list)
print("Type of list:", type(marks_list))
print("Marks (tuple):", marks_tuple)
print("Type of tuple:", type(marks_tuple))

# 3. Highest and lowest marks using built-in functions
highest_mark = max(marks_list)
lowest_mark = min(marks_list)
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)

# 4. Count students who scored at least 40.
# Each comparison gives True (1) or False (0), so adding them gives the count.
passed_count = (
    (marks_list[0] >= 40)
    + (marks_list[1] >= 40)
    + (marks_list[2] >= 40)
    + (marks_list[3] >= 40)
    + (marks_list[4] >= 40)
)
print("Students who scored at least 40:", passed_count)

# 5. Check that all marks are within 0 to 100.
# If the lowest is >= 0 and the highest is <= 100, every mark is in range.
all_valid = lowest_mark >= 0 and highest_mark <= 100
print("All marks within 0 to 100:", all_valid)

# 6. Changing one element in the list and one in the tuple
marks_list[1] = 45
print("List after changing index 1:", marks_list)

# The next line is commented out because it would crash the program with
# "TypeError: 'tuple' object does not support item assignment".
# marks_tuple[1] = 45

# Observation: A list is MUTABLE, so its elements can be changed after
# creation (the list changed from 35 to 45 successfully). A tuple is
# IMMUTABLE, so trying to change one of its elements raises a TypeError.
# Use a list when data needs to change and a tuple when it should stay fixed.
print("Tuple is unchanged:", marks_tuple)
