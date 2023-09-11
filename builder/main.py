from builder.Calculator import Calculator
from builder.User import *

if __name__ == '__main__':
    user = User.UserBuilder().name('asdf').password('1234').email('email@email.com').tell('010-1234-5678').builder()
    print(user)

    val = Calculator(10).add(10).add(10).subtract(5).divide(3).end()
    print("(10 + 10 - 5) / 3 = ", val)
