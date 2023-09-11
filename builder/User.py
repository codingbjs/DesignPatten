class User:
    def __init__(self, builder):
        self.__name = builder.name
        self.__password = builder.password
        self.__email = builder.email
        self.__tell = builder.tell

    def __str__(self):
        return f"{self.__name}, {self.__password}, {self.__email} ,{self.__tell}"

    class UserBuilder:

        def name(self, name):
            self.name = name
            return self

        def password(self, password):
            self.password = password
            return self

        def email(self, email):
            self.email = email
            return self

        def tell(self, tell):
            self.tell = tell
            return self

        def builder(self):
            return User(self)
