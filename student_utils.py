"""
student_utils.py
Utility functions for calculating student marks and grades.
Lecture 8: Fixing a Buggy Python Script Using AI (Corrected Implementation)
"""

PASS_MARK = 40


def calculate_average(marks):
    """
    Calculate the average of a list of marks.
    FIX 1: Divide by len(marks) instead of len(marks) - 1.
    """
    total = sum(marks)
    return total / len(marks)


def is_passing(mark):
    """
    Check if a mark is considered passing.
    FIX 2: Use >= comparison to include boundary mark (40).
    """
    return mark >= PASS_MARK


def get_grade(mark):
    """
    Return grade classification based on mark.
    FIX 3: Check highest threshold (>= 90 Distinction) before (>= 60 First).
    """
    if mark >= 90:
        return "Distinction"
    elif mark >= 60:
        return "First"
    elif mark >= 45:
        return "Second"
    else:
        return "Fail"
