# tuple = collection which is ordered and unchangeable
# used to group together related data

students = ("Felipe",28,"male")

print(students.count("Felipe"))
print(students.index("male"))

for i in students:
    print(i)
if "Felipe" in students:
    print("Felipe is here!")
