from unittest import TestCase

from v1.quicksort_v1 import quicksort as v1
from v2.quicksort_v2 import quicksort as v2
from v3.quicksort_v3 import quicksort as v3
from v4.quicksort_v4 import quicksort as v4

class QuicksortTests(TestCase):

    def setUp(self):
        self.v = v4  # Edit this line to test a different version

    def test_empty_list(self):
        a = []
        self.v(a)
        self.assertEqual(
            [],
            a
        )

    def test_single_element(self):
        a = [4]
        self.v(a)
        self.assertEqual(
            [4],
            a
        )

    def test_two_elements(self):
        a = [1, 2]
        self.v(a)
        self.assertEqual(
            [1, 2],
            a
        )

    def test_simple_sort(self):
        a = [2, 3, 4, 1]
        self.v(a)
        self.assertEqual(
            [1, 2, 3, 4],
            a
        )

    def test_simple_already_sorted(self):
        a = [1, 2, 3, 4]
        self.v(a)
        self.assertEqual(
            [1, 2, 3, 4],
            a
        )

    def test_odd_length(self):
        a = [5, 2, 3, 4, 1]
        self.v(a)
        self.assertEqual(
            [1, 2, 3, 4, 5],
            a
        )

    def test_duplicates(self):
        a = [2, 1, 2, 2]
        self.v(a)
        self.assertEqual(
            [1, 2, 2, 2],
            a
        )

    def test_big_sort(self):
        a = [3, 4, 1, 5, 8, 6, 9, 7, 2]
        self.v(a)
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            a
        )