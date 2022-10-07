
class FuelSystem:
    '''Топливна система'''
    def __init__(self, fuel, fuel_type):
        self.fuel = fuel
        self.fuel_type = fuel_type
        self.fuel_capacity = 40
        self.current_fuel_capacity = 0 + self.fuel
        self.available_fuel_type = ['gasoline', 'gas', 'diesel']

    def refuel(self, add_fuel=0): # заправити
        # if 0 < self.fuel <= self.fuel_capacity and self.fuel_type in self.available_fuel_type:
        #     print('good')
        # else:
        #     print('bad')
        if self.fuel >= 0:
            if self.fuel_type in self.available_fuel_type:
                x = self.current_fuel_capacity + add_fuel
                print(f'В баці: {self.current_fuel_capacity}л.\nЗаправлено на: {add_fuel}л.\nСума: {x}л')
            else:
                print(f'не правильний тип палива')
        else:
            print('не можлива операція!')

    def drain(self, drain_fuel=0): # злити
        if self.current_fuel_capacity >= drain_fuel:
            drain_f = self.current_fuel_capacity - drain_fuel
            print(f'В баці: {self.current_fuel_capacity}л.\nЗлито: {drain_fuel}л.\nСума: {drain_f}л')
        else:
            print('не можлива операція!')

f = FuelSystem(0, 'gasoline')
f.drain(0)
