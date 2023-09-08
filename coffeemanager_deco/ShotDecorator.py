from Coffee import Coffee


class ShotDecorator(Coffee):
    def __init__(self, coffee):
        super().__init__(coffee.get_name(),
                         coffee.get_stock(),
                         coffee.get_total_sales_cnt(),
                         coffee.get_safety_stock(),
                         coffee.get_cost(),
                         coffee.get_price())
        self.__coffee = coffee
        self.__name = self.__coffee.get_name() + '[shot]'
        self.__topping_price = 500

    def get_price(self):
        return self.__coffee.get_price() + self.__topping_price

    def offer(self, order_cnt):
        self.__coffee.__deduct_stock(order_cnt)  # 재고차감
        self.__coffee.__add_total_sales_cnt(order_cnt)  # 판매량 추가

        if self.__coffee.__stock < self.__coffee.__safety_stock:
            self.__coffee.__add_safety_stock()  # 안전재고 확보

    def add_stock(self, cnt):
        self.__coffee.__stock += cnt

    def get_stock(self):
        return self.__coffee.__stock

    def get_total_sales_cnt(self):
        return self.__coffee.__total_sales_cnt
