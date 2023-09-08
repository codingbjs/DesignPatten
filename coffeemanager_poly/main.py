from Menu import *
from coffeemanager_poly.SeasonCoffee import SeasonCoffee


def main():
    drinks = [
        Coffee("아메리카노", 10, 0, 3, 2000, 3000),
        Coffee("모카", 10, 0, 3, 3000, 4000),
        Coffee("라떼", 10, 0, 3, 4000, 5000),
        SeasonCoffee("프라푸치노", 10, 0, 3, 4000, 5000, [6, 7, 8, 9]),
    ]

    Menu(Sales(), drinks).main_menu()


if __name__ == "__main__":
    main()
