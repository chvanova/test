import unittest
from func import min, max


class TestMin(unittest.TestCase):
    def test_empty_iter(self):
        self.assertRaises(ValueError, min([]))

    def test_digit(self):
        self.assertEqual(min(3, 4, 1, 9, 6, 0), 0)

    def test_list(self):
        self.assertEqual(min([3, 415, 1, 2, 9, -6, 0]), -6)

    def test_list_len(self):
        self.assertEqual(min([[3, 415], [1, 2, 9], []], key=len), [])

    def test_list_el(self):
        self.assertEqual(
            min([[3, 415], [1, 2, 9], [-6, 0, ]], key=lambda x: x[1]),
            [-6, 0]
        )

    def test_letters(self):
        self.assertEqual(min('d', 'i', 'f', 'j', 'c', 'a', 'w', 'b'), 'a')

    def test_str(self):
        self.assertEqual(min('qwertyuipb'), 'b')

    def test_strs_len(self):
        self.assertEqual(
            min('lliu', ' lliu', 'dmvfkvm', 'qwes', key=len),
            'lliu'
        )

    def test_dict_keys(self):
        self.assertEqual(
            min([{'name': 'Nina', 'age': 27, 'country': 'Czech Republic'},
                 {'name': 'Anna', 'age': 25, 'country': 'Japan'},
                 {'name': 'Alisa', 'age': 25, 'country': 'Kanada'},
                 {'name': 'Mila', 'age': 26, 'country': 'USA'}],
                key=lambda x: x['age']),
            {'name': 'Anna', 'age': 25, 'country': 'Japan'}
        )

class TestMax(unittest.TestCase):
    def test_empty_iter(self):
        self.assertRaises(ValueError, min([]))

    def test_digit(self):
        self.assertEqual(max(1, 0, 1.00, 5**5, -254, 4**5), 5**5)

    def test_list(self):
        self.assertEqual(max([-2, -2**8, 8]), 8)

    def test_list_len(self):
        list_test = [i for i in xrange(0, 15)]
        self.assertEqual(
            max([[3415, 10**4, 18], ['case']*15, [], list_test],
                key=len),
            ['case'] * 15
        )

    def test_list_el(self):
        self.assertEqual(
            max([[1,2,5,0.00011],[8,98.8,0.0001], [1,2,0.000111]],
                key=lambda x: x[2]),
            [1, 2, 5, 0.00011]
        )

    def test_letters(self):
        self.assertEqual(max('I', 'F', 'J', 'C', 'a', 'W', 'b'), 'b')

    def test_str(self):
        self.assertEqual(max('qwertYuipb'), 'w')

    def test_strs_len(self):
        self.assertEqual(max('lliu', ' lliu', 'dmvfkvm', 'qwes', key=len),
                         'dmvfkvm')

    def test_dict_keys(self):
        self.assertEqual(
            max([{'name': 'Nina', 'age': 17, 'country': 'Czech Republic'},
                 {'name': 'Anna', 'age': 25, 'country': 'Japan'},
                 {'name': 'Alisa', 'age': 25, 'country': 'Kanada'},
                 {'name': 'Mila', 'age': 26, 'country': 'USA'}],
                key=lambda x: x['name']),
            {'name': 'Nina', 'age': 17, 'country': 'Czech Republic'}
        )

if __name__ == '__main__':
    unittest.main()