
class ManagementSystem:
    """система управління"""
    '''v.1.1'''

    def __init__(self):
        self.parking_brake = True                                           # parking brake on (True)
        self.gas_pedal = False                                              # gas pedal released (False)
        self.stop_pedal = False
        self.clutch_pedal = False
        self.steering_wheel = 'forward'
        self.steering_wheel_positions = ['forward', 'left', 'right']
        self.gear_box_lever = 'neutral'
        self.gearbox_positions = ['neutral', 'first', 'revers']

    def roll_steering_wheel(self, positions):
        if positions == self.steering_wheel:
            print(f'Steering wheel position already {positions}!')
        elif positions in self.steering_wheel_positions:
            self.steering_wheel = positions
            print(f'Steering wheel turned: {positions}')
        else:
            print('wrong position steering wheel')

    def parking_brake_on_off(self, position):
        parking_brake_position = ['on', 'off']                             # on=T, off=F
        if position in parking_brake_position:
            if position == 'on' and not self.parking_brake:
                self.parking_brake = True
                print(f'Parking brake is {position}')
            elif position == 'on' and self.parking_brake:
                print('Parking brake already on!')

            elif position == 'off' and self.parking_brake:
                self.parking_brake = False
                print('Parking brake off!')
            elif position == 'off' and not self.parking_brake:
                print('Parking brake already off!!!')
        else:
            print('Wrong position!!!')

    def gas(self, position):
        gas_position = ['press', 'released']
        if position in gas_position:
            if not self.parking_brake:
                if position == 'released' and not self.gas_pedal:
                    print('Gas pedal already released')

                elif position == 'press' and self.gas_pedal:
                    print('Gas pedal already pressed!')

                else:
                    self.gas_pedal = True
                    print(f'Gas pedal is {position}!')
            else:
                print(f'You cannot start the movement because parking brake is on')
        else:
            print('Wrong position!!!')

    def stop(self, position):
        stop_position = ['press', 'released']
        if position in stop_position:
            if position == 'released' and not self.stop_pedal:
                print('Stop pedal already released')
            elif position == 'press' and self.stop_pedal:
                print('Gas pedal already pressed!')
            else:
                self.stop_pedal = True
                print(f'Stop pedal is {position}')
        else:
            print('Wrong position!!!')

    def clutch_pedal_on_off(self, position):
        clutch_pedal_position = ['press', 'released']
        if position in clutch_pedal_position:
            if position == 'press' and not self.clutch_pedal:
                self.clutch_pedal = True
                print(f'Clutch pedal is {position}ed')
            elif position == 'press' and self.clutch_pedal:
                print(f'Clutch pedal is already {position}ed!!!')

            elif position == 'released' and self.clutch_pedal:
                self.clutch_pedal = False
                print(f'Clutch pedal is {position}')

            elif position == 'released' and not self.clutch_pedal:
                print(f'Clutch pedal is already {position}!!!')
        else:
            print('Wrong position!!!')
w = ManagementSystem()



