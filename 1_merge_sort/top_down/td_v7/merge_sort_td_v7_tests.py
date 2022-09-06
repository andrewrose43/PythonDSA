from unittest import TestCase
from merge_sort_td_v7 import merge_sort

class MergeSortTDV7Test(TestCase):

    def test_empty_list(self):
        a = []
        merge_sort(a)
        self.assertEqual(
            [],
            a
        )

    def test_single_element(self):
        a = [4]
        merge_sort(a)
        self.assertEqual(
            [4],
            a
        )

    def test_two_elements(self):
        a = [2, 1]
        merge_sort(a)
        self.assertEqual(
            [1, 2],
            a
        )

    def test_simple_sort(self):
        a = [2, 3, 4, 1]
        merge_sort(a)
        self.assertEqual(
            [1, 2, 3, 4],
            a
        )

    def test_simple_already_sorted(self):
        a = [1, 2, 3, 4]
        merge_sort(a)
        self.assertEqual(
            [1, 2, 3, 4],
            a
        )

    def test_odd_length(self):
        a = [5, 2, 3, 4, 1]
        merge_sort(a)
        self.assertEqual(
            [1, 2, 3, 4, 5],
            a
        )

    def test_duplicates(self):
        a = [2, 1, 2, 2]
        merge_sort(a)
        self.assertEqual(
            [1, 2, 2, 2],
            a
        )

    def test_big_sort(self):
        a = [3, 4, 1, 5, 8, 6, 9, 7, 2]
        merge_sort(a)
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            a
        )