import unittest
from main import Mammals

class ParentClassTest(unittest.TestCase):
    def setUp(self):
        self.animal_m = Mammals(min_num=1, max_num=300, units='кг', value=150, gender="м")
        self.animal_w = Mammals(min_num=1, max_num=300, units='кг', value=150, gender="ж")
        self.animal_m2 = Mammals(min_num=1, max_num=300, units='кг', value=150, gender="м")

    def test_method_check(self):
        num_min = 0
        num_max = 1000
        value = 300

        result = Mammals.check(num_min, num_max, 'м', value)
        self.assertEqual(result, value)

        value = 1010
        self.assertRaises(ValueError, Mammals.check, num_min, num_max, 'м', value)

    def test_method_check_str(self):
        lst = ["т", "е", "с", "т"]
        value = 'т'

        result = Mammals.check_str(lst, value)
        self.assertEqual(result, value)

        value = 'j'
        self.assertRaises(ValueError, Mammals.check_str, lst, value)

    def test_getter(self):
        result = self.animal_m.weight
        self.assertEqual(result, 150)

        result = self.animal_m.gender
        self.assertEqual(result, 'м')

    def test_setter(self):
        invalid_value = None
        with self.assertRaises(AttributeError):
            self.animal_m.gender = invalid_value
            self.animal_m.settings = invalid_value

    def test_reproduces_offspring(self):
        self.assertRaises(TypeError, Mammals.reproduces_offspring, self.animal_m, self.animal_m2)

        child = Mammals.reproduces_offspring(self.animal_m, self.animal_w)
        self.assertEqual(type(child), type(self.animal_m))

    def test_repr(self):
        self.assertEqual(repr(self.animal_m), 'Mammals(gender=м, weight=150)')

    def test_data_child(self):
        self.assertEqual(self.animal_m.data_child()[0], 'Mammals')

        lst_check_num = list(range(1, 6))
        lst_check_str = ["м", "ж"]

        




if __name__ == '__main__':
    unittest.main()
