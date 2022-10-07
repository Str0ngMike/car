
class CoolingSystem:
    '''Система охолодження'''

    def __init__(self, liquid, amount):
        self.liquid = liquid
        self.amount = amount
        self.min_amount = 5

    def cool_engine(self):
        '''охолодження двигуна'''
        if self.liquid == 'coolant' or self.liquid == 'water':

            if self.min_amount <= self.amount <= 10:
                return f'Сooling the engine by {self.liquid}!'
            elif self.amount > 10:
                raise Exception('The Cooling system has too much liquid')
            else:
                raise Exception('The Cooling system is empty or not enough')
        else:
            raise Exception('The Cooling system takes only water or coolant')


rad = CoolingSystem('water', 7)
print(rad.cool_engine())

