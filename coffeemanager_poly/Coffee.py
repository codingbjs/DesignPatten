from Purchase import *


class Coffee:
    def __init__(self, name, stock, total_sales_cnt, safety_stock, cost, price):
        self.__name = name
        self.__stock = stock
        self.__total_sales_cnt = total_sales_cnt
        self.__safety_stock = safety_stock
        self.__cost = cost
        self.__price = price

    def offer(self, order_cnt):
        self.__stock -= order_cnt
        self.__total_sales_cnt += order_cnt

        if self.__stock < self.__safety_stock:
            print('[system:log] 재고가 부족해 안전재고를 확보합니다.')
            purchase = Purchase(self, self.__safety_stock * 2)

            if purchase.execute():
                print('[system:log] 안전재고 확보에 성공했습니다.')
            else:
                print('[system:log] 안전재고 확보에 실패했습니다.')

    def add_stock(self, cnt):
        self.__stock += cnt

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        self.__stock = stock

    def get_total_sales_cnt(self):
        return self.__total_sales_cnt

    def set_total_sales_cnt(self, total_sales_cnt):
        self.__total_sales_cnt = total_sales_cnt

    def get_safety_stock(self):
        return self.__safety_stock

    def set_safety_stock(self, safety_stock):
        self.__safety_stock = safety_stock

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return (
                "Coffee [name="
                + self.__name
                + ", stock="
                + str(self.__stock)
                + ", totalSalesCnt="
                + str(self.__total_sales_cnt)
                + ", safetyStock="
                + str(self.__safety_stock)
                + ", cost="
                + str(self.__cost)
                + ", price="
                + str(self.__price)
                + "]"
        )
