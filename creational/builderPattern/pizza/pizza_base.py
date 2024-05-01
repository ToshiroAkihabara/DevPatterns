

class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        self.cooking_time = None

    def __str__(self):
        info: str = (
            f"Pizza name: {self.name}\n"
            f"Dough type: {self.dough.DoughDepth.name} & "
            f"{self.dough.DoughType.name}\n"
            f"Sauce type: {self.sauce}\n"
            f"Topping: {[t.name for t in self.topping]}\n"
            f"Cooking time: {self.cooking_time} minutes"
        )
        return info



