"""
test_student_utils.py
Unit tests for student_utils.py according to Lecture 8 requirements.
Contains EXACTLY 9 tests.
"""

import unittest
from student_utils import calculate_average, is_passing, get_grade


class TestStudentUtils(unittest.TestCase):

    # 1. Average of three marks — [80, 90, 100] -> 90.0
    def test_average_three_marks(self):
        marks = [80, 90, 100]
        self.assertEqual(calculate_average(marks), 90.0)

    # 2. Average of one mark — [40] -> 40.0
    def test_average_one_mark(self):
        marks = [40]
        self.assertEqual(calculate_average(marks), 40.0)

    # 3. Average of two marks — [50, 70] -> 60.0
    def test_average_two_marks(self):
        marks = [50, 70]
        self.assertEqual(calculate_average(marks), 60.0)

    # 4. Pass boundary — 40 -> True
    def test_pass_boundary(self):
        self.assertTrue(is_passing(40))

    # 5. Fail below boundary — 39 -> False
    def test_fail_below_boundary(self):
        self.assertFalse(is_passing(39))

    # 6. Pass above boundary — 75 -> True
    def test_pass_above_boundary(self):
        self.assertTrue(is_passing(75))

    # 7. Distinction — 95 -> "Distinction"
    def test_grade_distinction(self):
        self.assertEqual(get_grade(95), "Distinction")

    # 8. First — 65 -> "First"
    def test_grade_first(self):
        self.assertEqual(get_grade(65), "First")

    # 9. Second — 50 -> "Second"
    def test_grade_second(self):
        self.assertEqual(get_grade(50), "Second")


if __name__ == "__main__":
    unittest.main()
