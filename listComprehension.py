# list comprehension = a way to create a new list with less syntax
#                      can miminc certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in if conditional]
#                      list = [expression if/else for item iterable]

squares = []                        #create an empty list
for i in range(1, 11):              #create a for loop
    squares.append(i * i)           #define what each loop iteration should do
print(squares)

squares = [i * i for i in range(1, 11)]     # list comprehension
print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

# passed_students = list(filter(lambda x: x >= 60, students))

# passed_students = [i for i in students if i >= 60]     list comprehension - if statement

passed_students = [i if i >= 60 else "FAILED" for i in students]    # list comprehension - if/else statement

print(passed_students)
