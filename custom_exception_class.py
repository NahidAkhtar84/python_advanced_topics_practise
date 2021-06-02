
class CoffeeHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeeColdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CofeeCup:
    def __init__(self, temp):
        self.temperature = temp

    def coffeeTemp(self):
        if self.temperature > 80:
            raise CoffeeHotException('The coffee is hot!')

        elif self.temperature < 20:
            raise CoffeeColdException('The Coffee is cold!')

        else:
            raise Exception('The coffee is moderate!')

    
test1 = CofeeCup(120)
test1.coffeeTemp()