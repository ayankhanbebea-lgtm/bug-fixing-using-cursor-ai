"""
student_utils.py
Utility functions for calculating student marks and grades.
Lecture 8: Fixing a Buggy Python Script Using AI
"""

PASS_MARK = 40


def calculate_average(marks):
    """
    Calculate the average of a list of marks.
    BUG 1: Incorrectly divides by (len(marks) - 1).
    """
    total = sum(marks)
    return total / (len(marks) - 1)


def is_passing(mark):
    """
    Check if a mark is considered passing.
    BUG 2: Uses strict inequality '>' instead of '>='.
    """
    return mark > PASS_MARK


def get_grade(mark):
    """
    Return grade classification based on mark.
    BUG 3: First (>= 60) is checked before Distinction (>= 90).
    """
    if mark >= 60:
        return "First"
    elif mark >= 90:
        return "Distinction"
    elif mark >= 45:
        return "Second"
    else:
        return "Fail"
