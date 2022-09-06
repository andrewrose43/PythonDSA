from unittest import TestCase
from merge_sort_td_v1 import merge_sort

class MergeSortTDV1Test(TestCase):

    def test_empty_list(self):
        self.assertEqual(
            [],
            merge_sort([])
        )

    def test_single_element(self):
        self.assertEqual(
            [4],
            merge_sort([4])
        )

    def test_two_elements(self):
        self.assertEqual(
            [1, 2],
            merge_sort([2, 1])
        )

    def test_simple_sort(self):
        self.assertEqual(
            [1, 2, 3, 4],
            merge_sort([2, 3, 4, 1])
        )

    def test_simple_already_sorted(self):
        self.assertEqual(
            [1, 2, 3, 4],
            merge_sort([1, 2, 3, 4])
        )


    def test_odd_length(self):
        self.assertEqual(
            [1, 2, 3, 4, 5],
            merge_sort([5, 2, 3, 4, 1])
        )

    def test_duplicates(self):
        self.assertEqual(
            [1, 2, 2, 2],
            merge_sort([2, 1, 2, 2])
        )

    def test_big_sort(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            merge_sort([3, 4, 1, 5, 8, 6, 9, 7, 2])
        )

