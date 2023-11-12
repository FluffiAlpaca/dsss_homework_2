import unittest
from math_quiz import rand_int_gen, rand_oper_gen, rand_answer


class TestMathGame(unittest.TestCase):

    def test_rand_int_gen(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int_gen(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rand_oper_gen(self):
        # TODO
        oper = rand_oper_gen()
        self.assertTrue(oper == '+' or '-' or '*' or '/')
        pass

    def test_rand_answer(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()