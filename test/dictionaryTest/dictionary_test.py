import unittest

from dictionary.dictionary import my_dictionary


class MyTestCase(unittest.TestCase):
    def test_function_collects_word(self):
        character_count= my_dictionary("timothy")

    def test_function_returns_keyvalupair_and_not_repeat(self):
        character= my_dictionary("aawe")
        self.assertEqual(character,{'a':2,'w':1,'e':1})

    def test_function_returns_keyvalupair_of_numbers(self):
        character= my_dictionary(1123)
        self.assertEqual(character,{'1':2,'2':1,'3':1})

    def test_function_can_ignore_case(self):
        character= my_dictionary("AaAdvV")
        self.assertEqual(character,{'a':3,'d':1,'v':2})

    def test_function_can_count_symbols(self):
        character= my_dictionary("###$")
        self.assertEqual(character,{'#':3,'$':1})

    def test_function_can_ignore_space(self):
        character= my_dictionary("  a  ")
        self.assertEqual(character,{'a':1})