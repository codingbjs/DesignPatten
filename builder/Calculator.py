class Calculator:

    def __init__(self, result):
        self.__result = result

    def __str__(self):
        return f"{self.__result}"

    def add(self, num):
        self.__result += num
        return self

    def subtract(self, num):
        self.__result -= num
        return self

    def mutil(self, num):
        self.__result *= num
        return self

    def divide(self, num):
        self.__result /= num
        return self

    def end(self):
        return self
