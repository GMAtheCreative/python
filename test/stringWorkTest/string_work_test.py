import unittest
from stringWork.string_work_function import *


class TestString(unittest.TestCase):
    def test_string_can_output_2_strings_as_1_with_switched_last_letters(self):
        result = string_function("abc", "xyz")
        self.assertEqual(result, "abz xyc")

    def test_string_can_output_string_more_than_3_characters(self):
        result = string_function("hdgdk", "xyzhj")
        self.assertEqual(result, "hdgdj xyzhk")

    def test_string_output_1_char(self):
        result = string_function("a", "x")
        self.assertEqual(result, "x a")

    def test_string_can_add_ce_after_every_char3(self):
        result = string_functions("joy")
        self.assertEqual(result, "joyce")

    def test_string_can_add_ce_even_to_string_greater_3_characters(self):
        result = string_functions("hello")
        self.assertEqual(result, "helcelo")

    def test_string_can_output_caps_first(self):
        result = string_function1("sEmiColOn")
        self.assertEqual(result, "ECOsmioln")

    def test_string_can_remove_special_characters(self):
        result = string_function2("t,imo.th/y")
        self.assertEqual(result, "timothy")

    def test_string_can_return_tuple(self):
        result = string_function3("semicolon")
        self.assertEqual(result, ('o',2))
