class AirConditioner:
    def __init__(self):
        self.is_on = False
        self.temperature = 20

    def switch_on(self):
        self.is_on = True

    def switch_off(self):
        self.is_on = False

    def increase_temperature(self, increase_by):
        if self.is_on:
            self.temperature = min(30, self.temperature + increase_by)

    def decrease_temperature(self, decrease_by):
        if self.is_on:
            self.temperature = max(16, self.temperature - decrease_by)

    def get_status(self):
        return "ON" if self.is_on else "OFF"

    def get_temperature(self):
        return self.temperature