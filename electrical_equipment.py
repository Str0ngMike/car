class ElectricalEquipment:
    '''електрообладнання'''
    '''v.1.1'''
    def __init__(self):
        self.ligt_position = False
        self.emergency_signal_position = False
        self.battery = True
        self.headlights = 4

    def ligts_on(self):
        if self.battery:
            if not self.ligt_position:
                self.ligt_position = True
                print('Ligts on!')
            else:
                print('Ligts alredy on!!!')
        else:
            print('The battery is discharged!')

    def ligts_off(self):
        if self.ligt_position:
            self.ligt_position = False
            print('Ligts off!')
        else:
            print('Ligts alredy off!!!')

    def turn_signals_left(self):
        if self.battery:
            print('Turns ignals left on!')
        else:
            print('The battery is discharged!')

    def emergency_signal_on(self):
        if self.battery:
            if not self.emergency_signal_position:
                self.emergency_signal_position = True
                print('Emergency signal on!')
            else:
                print('Emergency signal alredy on!!!')
        else:
            print('The battery is discharged!')

    def emergency_signal_off(self):
        if self.battery:
            if self.emergency_signal_position:
                self.emergency_signal_position = False
                print('Emergency signal off!')
            else:
                print('Emergency signal alredy off!!!')
        else:
            print('The battery is discharged!')

    def turn_signals_right(self):
        if self.battery:
            print('Turns ignals right on!')
        else:
            print('The battery is discharged!')

s = ElectricalEquipment()
s.emergency_signal_on()
s.emergency_signal_off()
