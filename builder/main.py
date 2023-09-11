from builder.User import *

if __name__ == '__main__':
    user = User.UserBuilder().name('asdf').password('1234').email('email@email.com').tell('010-1234-5678').builder()
    print(user)
