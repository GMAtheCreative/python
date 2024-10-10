import unittest

from aircondition.air_condition import AirConditioner


class TestAirConditioner(unittest.TestCase):
    def setUp(self):
        self.aircon = AirConditioner()
        self.aircon.switch_on()

    def test_increase_temperature(self):

        self.aircon.increase_temperature(5)
        self.assertEqual(self.aircon.get_temperature(), 25)

    def test_decrease_temperature(self):
        self.aircon.increase_temperature(10)
        self.assertEqual(self.aircon.get_temperature(), 30)
        self.aircon.decrease_temperature(5)
        self.assertEqual(self.aircon.get_temperature(), 25)

    def test_temperature_limit(self):
        self.aircon.increase_temperature(15)
        self.assertEqual(self.aircon.get_temperature(), 30)


    def test_temperature_minimum(self):
        self.aircon.decrease_temperature(10)
        self.assertEqual(self.aircon.get_temperature(), 16)