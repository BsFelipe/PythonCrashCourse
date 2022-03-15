# filter() = creates a collection of elements from an iterable for which a function returns
# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 21)]

age = lambda data: data[1] >= 18

drinking_buddies = filter(age, friends)

for i in drinking_buddies:
    print(i)
