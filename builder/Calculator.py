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

    def multiply(self, num):
        self.__result *= num
        return self

    def divide(self, num):
        if num == 0:
            raise ValueError("Division by zero is not allowed.")
        self.__result /= num
        return self

    def end(self):
        return self.__result
