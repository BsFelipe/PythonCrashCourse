# sort() method = used with lists
# sort() function = used with iterables

#students = ("felipe", "Alex", "Boot", "Douglas", "Carioca")

# students.sort(reverse=True) #only list, not tupple
# sorted_students = sorted(students,reverse=True)

#level 2

students = (("Felipe", "A", 29),
            ("Alex", "F", 30),
            ("Douglas", "C", 27),
            ("Boot", "D", 28),
            ("Carioca", "B", 31))

# grade = lambda grades: grades[1] - order by GRADES
# students.sort(key=age, reverse=False) - sort list
# sorted tupples of tuppples
age = lambda ages: ages[2]
sorted_students = sorted(students, key=age, reverse=False)

for i in sorted_students:
    print(i)