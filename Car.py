class Car:
    name = 'test model'
    color = 'Grey'

    wheels = 4
    wheels_type = 'summer'

    def engine(self, status):
        if type(status) == int:
            return 'status must be \'on\' or \'off\''
        elif status.upper() == 'ON':
            return 'engine ON'
        elif status.upper() == 'OFF':
            return 'engine OFF'
        else:
            return 'status must be \'on\' or \'off\''

    def drive(self):
        return 'Drive!'

    def change_color(self, color):
        Car.color = color
        return f'color changed! \nnew color: {Car.color}'

    def change_wheels(self, change_wheels_type):
        if change_wheels_type != 'summer' and change_wheels_type != 'winter' and change_wheels_type != 'all season':
            return 'Wrong type of wheels!'
        elif type(change_wheels_type) == int:
            return 'Wrong type of wheels!'
        else:
            if self.wheels_type == change_wheels_type:
                return 'You alredy have summer wheels!'
            elif self.wheels_type != change_wheels_type:
                self.wheels_type = change_wheels_type
                return 'Wheels changed!'

first_car = Car()
print(first_car.change_wheels('all season'))
print(first_car.wheels_type)

