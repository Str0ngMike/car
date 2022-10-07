
class InjectionSystem:
    '''Система вприску'''

    def __init__(self, fuel=0):
        self.fuel = fuel
        self.max_fuel = 40

    def injection(self):
        if self.fuel <= 0:
            raise Exception('Not enough fuel')
        elif self.fuel > self.max_fuel:
            raise Exception('Too much fuel')
        else:
            return f'Injection!'

inj = InjectionSystem(30)
print(inj.injection())


