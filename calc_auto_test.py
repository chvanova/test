from pyvirtualdisplay import Display
from selenium import webdriver
import unittest

display = Display(visible=0, size=(800, 600))
display.start()


class TestCalc(unittest.TestCase):
    primary = 'http://127.0.0.1:8000/calculator/'
    error = 'http://127.0.0.1:8000/calculator/E/'


    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.primary)

    def tearDown(self):
        self.browser.close()

    def input_operand(self, *args):
        for i in str(args[0]):
            if i == '.':
                self.browser.find_element_by_id('11').click()
                continue
            self.browser.find_element_by_id(i).click()

    def input_operation(self, op):
        if op == '+':
            self.browser.find_element_by_id('13').click()
        if op == '-':
            self.browser.find_element_by_id('14').click()
        if op == '*':
            self.browser.find_element_by_id('16').click()
        if op == '/':
            self.browser.find_element_by_id('17').click()
        if op == '=':
            self.browser.find_element_by_id('12').click()
        if op == 'C':
            self.browser.find_element_by_id('18').click()
        if op == '#':
            self.browser.find_element_by_id('15').click()

    def test_title_str(self):
        self.assertEqual('Calculator', self.browser.title)

    def test_amount(self):
        a = 123
        b = 654
        self.input_operand(a)
        self.input_operation('+')
        self.input_operand(b)
        self.input_operation('=')
        url = self.browser.current_url
        self.assertEqual(url, self.primary + '{}/'.format(a+b))

    def test_subtraction(self):
        a = 987
        b = 789
        self.input_operand(a)
        self.input_operation('-')
        self.input_operand(b)
        self.input_operation('=')
        url = self.browser.current_url
        self.assertEqual(url, self.primary + '{}/'.format(a-b))

    def test_multiplication(self):
        a = 85.25
        b = 91
        self.input_operand(a)
        self.input_operation('*')
        self.input_operand(b)
        self.input_operation('=')
        url = self.browser.current_url
        self.assertEqual(url, self.primary + '{}/'.format(int(a*b)))

    def test_division(self):
        a = 13.12
        b = 1.991
        self.input_operand(a)
        self.input_operation('/')
        self.input_operand(b)
        self.input_operation('=')
        url = self.browser.current_url
        self.assertEqual(url, self.primary + '{}/'.format(int(a/b)))

    def test_division_zero(self):
        a = 999
        self.input_operand(a)
        self.input_operation('/')
        self.input_operand(0)
        self.input_operation('=')
        url = self.browser.current_url
        self.assertEqual(url,self.error)

    def test_divide_null(self):
        a = 0.1
        self.input_operand(0)
        self.input_operation('/')
        self.input_operand(a)
        self.input_operation('=')
        url = self.browser.current_url
        self.assertEqual(url, self.primary + '{}/'.format(int(0/a)))

    def test_clear_button(self):
        self.input_operand(8.888)
        self.input_operation('*')
        self.input_operation('C')
        url = self.browser.current_url
        self.assertEqual(url, self.primary)

    def test_sing_change(self):
        a = 77
        b = 11
        self.input_operand(a)
        self.input_operation('*')
        self.input_operand(b)
        self.input_operation('#')
        self.input_operation('=')
        url = self.browser.current_url
        self.assertEqual(url, self.primary + '{}/'.format(a*b*-1))

    def test_prioritizing(self):
        a = 333
        b = 777
        c = 11
        d = 4444
        self.input_operand(a)
        self.input_operation('+')
        self.input_operand(b)
        self.input_operation('#')
        self.input_operation('/')
        self.input_operand(c)
        self.input_operation('-')
        self.input_operand(d)
        self.input_operation('=')
        url = self.browser.current_url
        self.assertEqual(url, self.primary + '{}/'.format(a+b*-1/c-d))


if __name__ == '__main__':
    unittest.main()
