class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self, type, service):
        return f"Магазин продає {type}, і також {service}"

    def open_shop(self):
        return f"Онлайн-магазин {self.shop_name} відкритий"

    def number_of_units(self):
        return f"Кількість видів товару в магазині: {self.number_of_units}"

    def increment_number_of_units(self, number):
        return f"Кількість видів товару в магазині: {self.number_of_units + number}"
    pass


class Discount(Shop):
    def __init__(self, discount_products):
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        return f"Сьогоднішні товари по знижці: {self.discount_products}"
    pass


