class sale:

    def __init__(self, type, price, name, number):
        self.type = type
        self.price = price
        self.name = name
        self.number = number

    def sale_print(self):
        print("Sale")
        print("--------")
        print("ipad = ", self.type)
        print("Price = ", self.price)
        print("Name = ", self.name)
