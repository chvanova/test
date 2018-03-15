import unittest
from func import min


class TestMin(unittest.TestCase):
    def test_empty_iter(self):
        self.assertRaises(ValueError, min([]))

    def test_digit(self):
        self.assertEqual(min(3, 4, 1, 9, 6, 0), 0)

    def test_list(self):
        self.assertEqual(min([3, 415, 1, 2, 9, -6, 0]), -6)

    def test_list_len(self):
        self.assertEqual(min([[3, 415], [1, 2, 9], [-6, 0, ]], key=len),
                         [3, 415])

    def test_list_el(self):
        self.assertEqual(min([[3, 415], [1, 2, 9], [-6, 0, ]], key=lambda x: x[1]),
                         [-6, 0])

    def test_letters(self):
        self.assertEqual(min('d', 'i', 'f', 'j', 'c', 'a', 'w', 'b'), 'a')

    def test_str(self):
        self.assertEqual(min('qwertyuipb'), 'b')

    def test_strs_len(self):
        self.assertEqual(min('lliu', ' lliu', 'dmvfkvm', 'qwes', key=len), 'lliu')

    def test_dict_keys(self):
        self.assertEqual(min([{'name': 'Nina', 'age': 27, 'country': 'Czech Republic'},
                              {'name': 'Anna', 'age': 25, 'country': 'Japan'},
                              {'name': 'Alisa', 'age': 25, 'country': 'Kanada'},
                              {'name': 'Mila', 'age': 26, 'country': 'USA'}],
                             key=lambda x: x['age']), {'name': 'Anna', 'age': 25, 'country': 'Japan'})

class TestMax(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()