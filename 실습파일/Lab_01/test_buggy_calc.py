import unittest
from 실습파일.Lab_01.buggy_calc import calculate_final_price

class TestCalculateFinalPrice(unittest.TestCase):
    def test_decimal_discount(self):
        """0.2와 같은 소수점 입력 시 정상 계산되는지 확인"""
        self.assertEqual(calculate_final_price(10000, 0.2), 8000)

    def test_integer_discount(self):
        """20과 같은 정수 입력 시 20%로 처리되는지 확인"""
        self.assertEqual(calculate_final_price(10000, 20), 8000)

    def test_negative_discount(self):
        """음수 할인율 입력 시 할인이 적용되지 않는지(0%) 확인"""
        self.assertEqual(calculate_final_price(10000, -0.5), 10000)

    def test_excessive_discount(self):
        """100%를 초과하는 할인율 입력 시 무료(0)로 처리되는지 확인"""
        self.assertEqual(calculate_final_price(10000, 150), 0)
        self.assertEqual(calculate_final_price(10000, 1.5), 0)

    def test_boundary_zero_and_one(self):
        """0(0%)과 1(100%) 경계값 테스트"""
        self.assertEqual(calculate_final_price(10000, 0), 10000)
        self.assertEqual(calculate_final_price(10000, 1), 0)
        self.assertEqual(calculate_final_price(10000, 100), 0)

if __name__ == '__main__':
    unittest.main()