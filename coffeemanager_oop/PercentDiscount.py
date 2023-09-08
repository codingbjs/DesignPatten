class PercentDiscount:
    @staticmethod
    def cal_discount_order_price(order):
        discount = 0
        order_price = order.get_order_price()
        if order_price() >= 10000:
            discount = order_price * 0.1

        return discount
