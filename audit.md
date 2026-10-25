# Repository Audit Report

**Project Title**: FIXING A BUGGY PYTHON SCRIPT USING AI  
**Source of Truth**: Lecture 8 Instructions & Assignment Rubric  
**Target Repository**: `https://github.com/ayankhanbebea-lgtm/bug-fixing-using-cursor-ai`  
**Auditor**: Antigravity Pair Programmer / QA Auditor  
**Date of Audit**: October 25, 2026  

---

## 1. Executive Summary

This audit assesses the repository's adherence to the pedagogical guidelines and technical requirements specified in Lecture 8: *"Fixing a Buggy Python Script Using AI"*. The audit verifies the presence of all required files, inspects the original bugs and subsequent fixes, validates that exactly 9 unit tests exist without alteration, confirms preserved evidence across the **RED → FIX → GREEN** cycle, and assesses the Git commit history.

---

## 2. Item-by-Item Verification Checklist

### 1. Required Files
- [x] `student_utils.py`: Present. Contains `calculate_average`, `is_passing`, and `get_grade`.
- [x] `test_student_utils.py`: Present. Contains exactly 9 unit tests.
- [x] `README.md`: Present. Documents function descriptions, test execution instructions (`python test_student_utils.py`), test count (9), final pass status, and the RED → FIX → GREEN workflow.
- [x] `bug_notes.md`: Present. Contains a table documenting the 3 bugs with evidence, root causes, and fixes, alongside AI prompt transcripts.
- [x] `audit.md`: Present. Provides this comprehensive compliance audit.
- [x] RED / failing test evidence: Recorded in `evidence/red_test_output.txt`.
- [x] GREEN / passing test evidence: Recorded in `evidence/green_test_output.txt`.
- [x] AI debugging evidence: Documented in `bug_notes.md`.

---

### 2. Buggy Code Verification (Lecture 8 Alignment)
- [x] **Bug 1 (Average calculation)**:
  - Original flaw: Used `len(marks) - 1` as divisor.
  - Verification: `[80, 90, 100]` produced `135.0` instead of `90.0`; single mark `[40]` resulted in `ZeroDivisionError: division by zero`.
- [x] **Bug 2 (Passing boundary)**:
  - Original flaw: Used strict inequality `mark > PASS_MARK` where `PASS_MARK = 40`.
  - Verification: Score of `40` evaluated to `False`; `39` evaluated to `False`; `75` evaluated to `True`.
- [x] **Bug 3 (Grade ordering)**:
  - Original flaw: Condition `mark >= 60` was checked before `mark >= 90`.
  - Verification: Score of `95` entered the `>= 60` branch and incorrectly returned `"First"` instead of `"Distinction"`.

---

### 3. Test Suite Integrity
- [x] Number of tests: Exactly **9 tests** using Python standard `unittest`.
- [x] Test cases covered:
  1. `test_average_three_marks`: `[80, 90, 100]` $\to$ `90.0`
  2. `test_average_one_mark`: `[40]` $\to$ `40.0`
  3. `test_average_two_marks`: `[50, 70]` $\to$ `60.0`
  4. `test_pass_boundary`: `40` $\to$ `True`
  5. `test_fail_below_boundary`: `39` $\to$ `False`
  6. `test_pass_above_boundary`: `75` $\to$ `True`
  7. `test_grade_distinction`: `95` $\to$ `"Distinction"`
  8. `test_grade_first`: `65` $\to$ `"First"`
  9. `test_grade_second`: `50` $\to$ `"Second"`
- [x] Test integrity: The unit tests were **not** modified, weakened, or bypassed to artificially force a pass.

---

### 4. RED Stage Evidence
- [x] The test suite was executed against the buggy implementation prior to editing code.
- [x] The execution resulted in 4 failures and 1 error:
  - `AssertionError: 135.0 != 90.0` (3 marks average)
  - `ZeroDivisionError: division by zero` (1 mark average)
  - `AssertionError: 120.0 != 60.0` (2 marks average)
  - `AssertionError: False is not true` (pass boundary at 40)
  - `AssertionError: 'First' != 'Distinction'` (mark 95)
- [x] Output captured in `evidence/red_test_output.txt`.

---

### 5. AI Debugging Methodology
- [x] Debugging utilized targeted AI review instead of blanket whole-file regeneration.
- [x] Followed four-step process per defect:
  1. Explain failing test.
  2. Identify likely root cause.
  3. Check proposed minimal fix.
  4. Review fixed solution.

---

### 6. FIX Stage Implementation
- [x] `calculate_average`: Updated to `return total / len(marks)`.
- [x] `is_passing`: Updated to `return mark >= PASS_MARK`.
- [x] `get_grade`: Reordered so `mark >= 90` is checked before `mark >= 60`.

---

### 7. GREEN Stage Verification
- [x] Executed unchanged test suite `python test_student_utils.py`.
- [x] Result:
  ```text
  .........
  ----------------------------------------------------------------------
  Ran 9 tests in 0.000s

  OK
  ```
- [x] Output captured in `evidence/green_test_output.txt`.

---

### 8. Git Commit History
- [x] Preserves historical commits without destructive rebasing.
- [x] Discrete stages represented:
  - Commit `129c44e`: `red: add buggy student_utils.py, 9 unit tests, and RED test failure evidence`
  - Current commit: `fix & green: implement targeted AI fixes, verify 9/9 tests pass, and add audit documentation`

---

## 3. Final Verification Result

- **Test execution command**: `python test_student_utils.py`
- **Tests ran**: 9
- **Failures**: 0
- **Errors**: 0
- **Overall Status**: **PASS (100% compliant with Lecture 8)**
