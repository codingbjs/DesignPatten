from Coffee import Coffee


class ChocoDecorator(Coffee):
    def __init__(self, coffee):
        super().__init__(coffee.get_name(),
                         coffee.get_stock(),
                         coffee.get_total_sales_cnt(),
                         coffee.get_safety_stock(),
                         coffee.get_cost(),
                         coffee.get_price())
        self.__coffee = coffee
        self.__name = self.__coffee.get_name() + '[choco]'
        self.__topping_price = 500

    def get_price(self):
        return self.__coffee.get_price() + self.__topping_price

    def offer(self, order_cnt):
        self.__coffee.offer(order_cnt) # 재고차감

    def add_stock(self, cnt):
        self.__coffee.__stock += cnt

    def get_stock(self):
        return self.__coffee.__stock

    def get_total_sales_cnt(self):
        return self.__coffee.__total_sales_cnt
