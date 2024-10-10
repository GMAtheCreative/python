import unittest


import unittest

from bike.bike import Bike


class TestBike(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()

    def test_bike_initial_state(self):
        self.assertFalse(self.bike.is_switch)
        self.assertEqual(self.bike.speed, 0)
        self.assertEqual(self.bike.gear, 0)

    def test_kick_start(self):
        self.bike.kick(1)
        self.assertTrue(self.bike.is_switch)

    def test_kick_stop(self):
        self.bike.kick(1)
        self.bike.kick(0)
        self.assertFalse(self.bike.is_switch)

    def test_acceleration(self):
        self.bike.kick(1)
        self.bike.set_acceleration(10)
        self.assertEqual(self.bike.speed, 11)
        self.assertEqual(self.bike.gear, 1)

    def test_deceleration(self):
        self.bike.kick(1)
        self.bike.set_acceleration(10)
        self.bike.set_deceleration(5)
        self.assertEqual(self.bike.speed, 6)

    def test_gear_shifting(self):
        self.bike.kick(1)
        self.bike.set_acceleration(25)  # Shift to gear 2
        self.assertEqual(self.bike.gear, 2)

    def test_gear_shifting_max(self):
        self.bike.kick(1)
        self.bike.set_acceleration(40)  # Shift to gear 4
        self.assertEqual(self.bike.gear, 4)

    def test_get_state_on(self):
        self.bike.kick(1)
        self.assertEqual(self.bike.get_state(), "VROOM")

    def test_get_state_off(self):
        self.assertEqual(self.bike.get_state(), "OFF")
