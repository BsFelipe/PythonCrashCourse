# zip(*iterables) = aggregate elements from two or more iterables (lists, tuples, sets, etc.)
#                   create a zip object with paired elements stored in tupples for each element

username = ["Felipe", "Joao", "Jose"]
passwords = ('cebola', 'bolo', 'feijão')
login_date = ['2021-10-10', '2021-10-11', '2021-10-12']

users = zip(username, passwords, login_date)

for i in users:
    print(i)

# dictionary
username = ["Felipe", "Joao", "Jose"]
passwords = ('cebola', 'bolo', 'feijão')

users = dict(zip(username, passwords))

for key, value in users.items():
    print(key+": "+value)
