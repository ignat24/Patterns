class SendOrder:

    def send_order(self):
        print("Sending order to McDonald's...")


class CookOrder:

    def cook_order(self):
        print("Cooking your order...")


class Delivery:

    def delivery(self):
        print("Looking for a delivery man...")


class DeliveredOrder:

    def delivered_order(self):
        print("Open your dor, please!")


class Glovo:

    def __init__(self):
        self.send = SendOrder()
        self.cook = CookOrder()
        self.delivery = Delivery()
        self.delivered = DeliveredOrder()

    def order_food(self):
        self.send.send_order()
        self.cook.cook_order()
        self.delivery.delivery()
        self.delivered.delivered_order()


client = Glovo()
client.order_food()