import unittest
from main import Product, IdCounter, COUNTER_FOR_PRODUCT


class ProductClassTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product1 = Product(name='Сыр "Василевский"', price=85.50, rating=72.10)
        cls.product2 = Product(name='Макароны "Итальянская фантазия"', price=73.00, rating=51.60)
        cls.product3 = Product(name='Консервы "Русский улов"', price=45.20, rating=63.85)
        cls.product4 = Product(name='Хлеб "Семейный"', price=25.00, rating=88.30)
        cls.product5 = Product(name='Яйца "Счастливая курочка"', price=50.40, rating=77.60)

    def test_getter(self):
        # test id
        result = self.product1.id
        self.assertEqual(result, 1)

        result = self.product2.id
        self.assertEqual(result, 2)

        result = self.product3.id
        self.assertEqual(result, 3)

        # test name
        result = self.product1.name
        self.assertEqual(result, 'Сыр "Василевский"')

        result = self.product2.name
        self.assertEqual(result, 'Макароны "Итальянская фантазия"')

        result = self.product3.name
        self.assertEqual(result, 'Консервы "Русский улов"')

        # test price
        result = self.product1.price
        self.assertEqual(result, 85.50)

        result = self.product2.price
        self.assertEqual(result, 73.00)

        result = self.product3.price
        self.assertEqual(result, 45.20)

        # test rating
        result = self.product1.rating
        self.assertEqual(result, 72.10)

        result = self.product2.rating
        self.assertEqual(result, 51.60)

        result = self.product3.rating
        self.assertEqual(result, 63.85)

    def test_setter(self):
        invalid_value = None
        with self.assertRaises(AttributeError):
            self.product1.name = invalid_value
            self.product2.name = invalid_value
            self.product3.name = invalid_value

            self.product1.id = invalid_value
            self.product2.id = invalid_value
            self.product3.id = invalid_value

            self.product1.zdfgdfg = invalid_value
            self.product2.fgjftjg = invalid_value
            self.product3.rgdrfg = invalid_value

        with self.assertRaises(ValueError):
            self.product1.price = invalid_value
            self.product2.price = invalid_value
            self.product3.price = invalid_value

        # test price
        invalid_value = 10000
        self.product1.price = invalid_value
        self.assertEqual(self.product1.price, 10000)

        self.product2.price = invalid_value
        self.assertEqual(self.product2.price, 10000)

        self.product3.price = invalid_value
        self.assertEqual(self.product3.price, 10000)

        # test rating
        self.product1.rating = invalid_value
        self.assertEqual(self.product1.rating, 10000)

        self.product2.rating = invalid_value
        self.assertEqual(self.product2.rating, 10000)

        self.product3.rating = invalid_value
        self.assertEqual(self.product3.rating, 10000)

    def test_method_check_attribute(self):
        types = (int, float)
        value = 300

        result = Product.check_attribute(value, types)
        self.assertEqual(result, value)

        value = '1010'
        self.assertRaises(ValueError, Product.check_attribute, value, types)

    def test_repr(self):
        self.assertEqual(repr(self.product1), 'Product(name=\'Сыр "Василевский"\', price=85.5, rating=72.1)')

    def test_str(self):
        self.assertEqual(str(self.product5), '5_[Яйца "Счастливая курочка"]')



if __name__ == '__main__':
    unittest.main()
