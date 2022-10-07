class Car:
    def __init__(self, engine):

        self.engine = engine

        self.isRunning = False

    def turnKey(self, direction):
        if direction == 'clockwise':
            Engine.start(self)
            print('Engine started')
        if direction == 'counterclockwise':
            Engine.stop(self)
            print('Engine stopped')


class Engine:

    def __init__(self, model, age, manufacturer, volume, cylinders):
        self.model = model
        self.age = age
        self.manufacturer = manufacturer
        self.volume = volume
        self.cylinders = cylinders

        self.isRunning = False  # add

    def start(self):
        if self.isRunning:
            raise Exception('Engine is already running!')
        else:
            self.isRunning = True
            return 'Engine started'  # add

    def stop(self):
        if self.isRunning:
            self.isRunning = False
        else:  # add
            raise Exception('Engine is already stoped!')  # add


engine_1 = Engine('B1', 2, 'honda', 1.8, 4)  # обєкт класу Engine


lada = Car('B1')
lada.turnKey('counterclockwise')