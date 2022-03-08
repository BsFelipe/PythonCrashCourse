email = input("Enter your e-mail: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 2:]

print(f"Your username is {username} & domain is {domain}")