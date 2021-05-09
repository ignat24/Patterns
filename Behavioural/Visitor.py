class GlovoVisitor:

    def action(self, method):
        methods = {
            Create: self.create_order,
            Cook: self.cook_order,
            Delivery: self.delivery_order
        }
        action = methods.get(type(method), self.order_error)
        action()

    def create_order(self):
        print("Create order")

    def cook_order(self):
        print("Cooking order")

    def delivery_order(self):
        print("Delivery your order")

    def order_error(self, method):
        print("Error order! Try again!")


class Method:

    def method(self, visitor):
        visitor.action(self)


class Create(Method):
    pass

class Cook(Method):
    pass


class Delivery(Method):
    pass


visitor = GlovoVisitor()

create = Create()
create.method(visitor)

cook = Cook()
cook.method(visitor)

delivery = Delivery()
delivery.method(visitor)



