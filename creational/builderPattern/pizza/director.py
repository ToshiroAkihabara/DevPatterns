from builder import Builder, MargaritaPizza, CheesePizza


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_pizza(self):
        if not self.builder:
            raise ValueError("Should set builder first")
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_topping()


if __name__ == "__main__":
    director = Director()
    for recept in (MargaritaPizza, CheesePizza):
        builder = recept()
        director.set_builder(builder)
        director.make_pizza()
        pizza = builder.get_pizza()
        print(pizza)
        print("------------------------")


