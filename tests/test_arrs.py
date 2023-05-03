import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1), 2)
        self.assertEqual(arrs.get([1, 2, 3], 1), 2)
        self.assertEqual(arrs.get([1, 2, 3], -1), 3)
        self.assertEqual(arrs.get([1, 2, 3], 3, 'default'), 'default')
        self.assertEqual(arrs.get([], 0, 'default'), 'default')
        self.assertEqual(arrs.get([1, 2, 3], -4, 'default'), 'default')

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 10), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -10), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice([]), [])

    def test_normalized_start_less_than_zero(self):
        # Test when start is less than 0
        coll = [1, 2, 3, 4, 5]
        start = -3
        end = None
        expected_result = [3, 4, 5]
        result = arrs.my_slice(coll, start, end)
        self.assertEqual(result, expected_result)

    def test_normalized_start_less_than_negative_length(self):
        # Test when start is less than negative length
        coll = [1, 2, 3, 4, 5]
        start = -7
        end = None
        expected_result = [1, 2, 3, 4, 5]
        result = arrs.my_slice(coll, start, end)
        self.assertEqual(result, expected_result)

    def test_normalized_start_plus_length(self):
        # Test when start plus length is greater than normalized_end
        coll = [1, 2, 3, 4, 5]
        start = 2
        end = 4
        expected_result = [3, 4]
        result = arrs.my_slice(coll, start, end)
        self.assertEqual(result, expected_result)

    def test_positive_indices(self):
        # проверка среза с положительными индексами
        arr = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(arrs.my_slice(arr, 1, 4), [2, 3, 4])

    def test_negative_start_index(self):
        # проверка среза со start < 0
        arr = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(arrs.my_slice(arr, -3, 6), [4, 5, 6])

    def test_negative_end_index(self):
        # проверка среза с end < 0
        arr = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(arrs.my_slice(arr, 0, -2), [1, 2, 3, 4])

    def test_negative_indices(self):
        # проверка среза с отрицательными start и end
        arr = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(arrs.my_slice(arr, -4, -2), [3, 4])

    def test_empty_list(self):
        # проверка среза пустого списка
        arr = []
        self.assertListEqual(arrs.my_slice(arr, 1, 3), [])

    def test_start_index_out_of_range(self):
        # проверка среза, когда start вне диапазона
        arr = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(arrs.my_slice(arr, 10, 15), [])

    def test_end_index_out_of_range(self):
        # проверка среза, когда end вне диапазона
        arr = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(arrs.my_slice(arr, 2, 10), [3, 4, 5, 6])

    def test_no_start_or_end_indices(self):
        # проверка среза без указания start или end
        arr = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(arrs.my_slice(arr), [1, 2, 3, 4, 5, 6])



