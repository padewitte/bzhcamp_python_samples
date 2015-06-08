import unittest

def fun(x,y):
    return x + y

class MyTest(unittest.TestCase):
    def setUp(self):
        self.inc = 1

    def test_premier(self):
        self.assertEqual(fun(3,self.inc), 4)

    def test_second(self):
        self.assertEqual(fun(3,self.inc), 'wrong')
