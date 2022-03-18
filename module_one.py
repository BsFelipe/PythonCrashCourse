# if __name__ = '__main__'

# 1.  module can be run as a standalone program
# or
# 2. module can be imported and used  by other modules

# Python interpreter sets "special variables", one which is __name__
# Python will assign the __name__ variable a value of '__main__'    if it's
# the initial module begin

def hello():
    print("hello")


if __name__ == '__main__':
    hello()

