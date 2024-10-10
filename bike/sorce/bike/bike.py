class Bike:
    def __init__(self):
        self.is_switch = False
        self.gear = 0
        self.speed = 0

    def kick(self, kick_value):
        if kick_value == 1:
            self.is_switch = True
        elif kick_value == 0:
            self.is_switch = False

    def set_acceleration(self, acceleration):
        if self.is_switch:
            self.speed = acceleration + 1
            if 0 < self.speed < 21:
                self.gear = 1
            elif 20 < self.speed < 31:
                self.speed = acceleration + 2
                self.gear = 2
            elif 30 < self.speed < 41:
                self.speed = acceleration + 3
                self.gear = 3
            elif self.speed == 41:
                self.speed = acceleration + 4
                self.gear = 4
            elif self.speed < 0 or self.speed > 41:
                self.gear = 0

    def set_deceleration(self, deceleration):
        if self.is_switch:
            self.speed -= deceleration

    def get_state(self):

        return "VROOM" if self.is_switch else "OFF"

    def get_speed(self):
        return self.speed

    def get_gear(self):
        return self.gear

