import unittest
from task3 import calculate_average_velocity


class TestVelocity(unittest.TestCase):
    def setUp(self) -> None:
        self.succesful_data = (100, 200, 300, 400)
        self.succesful_answer = 250.0

        self.wrong_data = (100, 200, 300, '400')

    def test_succesful(self):
        self.assertEqual(calculate_average_velocity(*self.succesful_data), self.succesful_answer)

    def test_wrong(self):
        self.assertRaises(TypeError, calculate_average_velocity,*self.wrong_data)


if __name__ == '__main__':
    unittest.main()