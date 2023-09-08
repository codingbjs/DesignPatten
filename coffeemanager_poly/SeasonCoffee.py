from datetime import datetime

from coffeemanager_poly.Coffee import Coffee


class SeasonCoffee(Coffee):
    def __init__(self, name, stock, total_sales_cnt, safety_stock, cost, price, season_month):
        super().__init__(name, stock, total_sales_cnt, safety_stock, cost, price)
        self.__season_month = season_month

    def is_season(self):
        now_month = datetime.now().month
        if now_month in self.__season_month:
            return True
        return False
