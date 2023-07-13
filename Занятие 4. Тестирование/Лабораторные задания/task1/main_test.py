import unittest
from main import Mammals


class ParentClassTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.animal_m = Mammals(min_num=1, max_num=300, units='кг', value=150, gender="м")
        cls.animal_w = Mammals(min_num=1, max_num=300, units='кг', value=150, gender="ж")
        cls.animal_m2 = Mammals(min_num=1, max_num=300, units='кг', value=150, gender="м")

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
        value = 'с'

        result = Mammals.check_str(lst, value)
        self.assertEqual(result, value)

        value = 'w'
        self.assertRaises(ValueError, Mammals.check_str, lst, value)

    def test_getter(self):
        result = self.animal_m.weight
        self.assertEqual(result, 150)

        result = self.animal_m.gender
        self.assertEqual(result, 'м')

        result = self.animal_m.data
        self.assertEqual(result, [1, 300, 'кг'])

    def test_setter(self):
        invalid_value = None
        with self.assertRaises(AttributeError):
            self.animal_m.data = invalid_value

        with self.assertRaises(AttributeError):
            self.animal_m.gender = invalid_value

        with self.assertRaises(ValueError):
            self.animal_m.weight = invalid_value

    def test_reproduces_offspring(self):
        self.assertRaises(TypeError, Mammals.reproduces_offspring, self.animal_m, self.animal_m2)

        child = Mammals.reproduces_offspring(self.animal_m, self.animal_w)
        self.assertEqual(type(child), type(self.animal_m))

    def test_repr(self):
        self.assertEqual(repr(self.animal_m), 'Mammals(gender=м, weight=150)')

    def test_data_child(self):
        data_child_te = self.animal_m.data_child()
        lst_check_num = list(range(1, 50))
        lst_check_str = ["м", "ж"]
        self.assertEqual(data_child_te[0], 'Mammals')
        self.assertIn(data_child_te[-1][-2], lst_check_num)
        self.assertIn(data_child_te[-1][-1], lst_check_str)

    def test_movement(self):
        text = self.animal_m.movement()

        self.assertEqual(text, f'Животное Mammals двигается')

    def test_eats(self):
        text = self.animal_m.eats()

        self.assertEqual(text, f'Животное Mammals кушает')


if __name__ == '__main__':
    unittest.main()
