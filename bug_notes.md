# Bug Notes: AI-Assisted Debugging (Lecture 8)

This document records the systematic identification, analysis, AI-assisted debugging, and targeted resolution of the three core bugs in `student_utils.py`, following the Lecture 8 workflow.

---

## 1. Summary Bug Table

| Bug # | Component / Function | Evidence / Failed Test | Root Cause | Targeted Fix Applied |
|:---:|:---|:---|:---|:---|
| **1** | `calculate_average(marks)` | • `[80, 90, 100]` returned `135.0` instead of `90.0`<br>• `[40]` raised `ZeroDivisionError: division by zero`<br>• `[50, 70]` returned `120.0` instead of `60.0` | Incorrect divisor calculation: `len(marks) - 1`. For a 1-element list, divisor is `0`. For $n > 1$, divides by $n - 1$. | Replaced divisor `len(marks) - 1` with `len(marks)`: `return total / len(marks)` |
| **2** | `is_passing(mark)` | • `is_passing(40)` returned `False` instead of `True` (failing pass boundary) | Strict inequality `mark > PASS_MARK` (`40 > 40` evaluates to `False`), excluding the minimum passing mark. | Changed comparison operator from `>` to `>=`: `return mark >= PASS_MARK` |
| **3** | `get_grade(mark)` | • `get_grade(95)` returned `"First"` instead of `"Distinction"` | Flawed conditional order: `mark >= 60` was evaluated before `mark >= 90`. Because 95 is $\ge 60$, it short-circuited into the First-class branch. | Reordered conditional ladder to check highest boundary first (`mark >= 90` before `mark >= 60`). |

---

## 2. Detailed AI Debugging Walkthrough

Following Lecture 8's interactive AI debugging methodology:
1. Explain the failing test.
2. Identify the likely bug with AI assistance.
3. Check and validate a proposed minimal targeted fix.
4. Review the fixed solution without rewriting the program blindly.

---

### Bug 1: Average Calculation

#### Failing Test Evidence:
```text
FAIL: test_average_three_marks (AssertionError: 135.0 != 90.0)
ERROR: test_average_one_mark (ZeroDivisionError: division by zero)
```

#### AI Debugging Interaction:
- **Prompt to AI**:
  > *"When running test_average_three_marks with `[80, 90, 100]`, the test failed with `135.0 != 90.0`. Additionally, `[40]` crashed with `ZeroDivisionError: division by zero`. Review `calculate_average` in `student_utils.py`. What is causing these errors and what is the minimal fix?"*
- **AI Response Summary**:
  > *"The bug is in the denominator: `return total / (len(marks) - 1)`. In sample statistics, sample variance uses $n-1$ degrees of freedom (Bessel's correction), but the arithmetic mean of a dataset must always divide by the count $n$, i.e., `len(marks)`. For $n=1$, `len(marks) - 1 == 0`, triggering a ZeroDivisionError. For $n=3$, $270 / 2 = 135.0$. Replace `total / (len(marks) - 1)` with `total / len(marks)`."*

#### Fix Applied:
```python
# Before
return total / (len(marks) - 1)

# After
return total / len(marks)
```

---

### Bug 2: Pass Boundary Condition

#### Failing Test Evidence:
```text
FAIL: test_pass_boundary (AssertionError: False is not true)
```

#### AI Debugging Interaction:
- **Prompt to AI**:
  > *"Test `test_pass_boundary` asserts that `is_passing(40)` is True where `PASS_MARK = 40`. However, `is_passing(40)` returns `False`. Please analyze the operator logic."*
- **AI Response Summary**:
  > *"In `student_utils.py`, the condition is written as `mark > PASS_MARK`. A pass mark is inclusive: achieving exactly 40 points constitutes a pass. With strict inequality, `40 > 40` evaluates to `False`. The fix is to change `>` to `>=`."*

#### Fix Applied:
```python
# Before
return mark > PASS_MARK

# After
return mark >= PASS_MARK
```

---

### Bug 3: Grade Classification Ordering

#### Failing Test Evidence:
```text
FAIL: test_grade_distinction (AssertionError: 'First' != 'Distinction')
```

#### AI Debugging Interaction:
- **Prompt to AI**:
  > *"For a mark of 95, `get_grade(95)` returned `'First'` instead of `'Distinction'`. Why is the elif condition for Distinction not executing?"*
- **AI Response Summary**:
  > *"In an `if / elif / else` ladder, conditions are evaluated sequentially from top to bottom. The first condition is `if mark >= 60: return 'First'`. Because 95 is greater than 60, the branch triggers immediately and returns `'First'`, preventing the subsequent `elif mark >= 90:` branch from ever being reached. Multi-tiered numerical thresholds must be ordered from highest to lowest."*

#### Fix Applied:
```python
# Before
if mark >= 60:
    return "First"
elif mark >= 90:
    return "Distinction"
elif mark >= 45:
    return "Second"
else:
    return "Fail"

# After
if mark >= 90:
    return "Distinction"
elif mark >= 60:
    return "First"
elif mark >= 45:
    return "Second"
else:
    return "Fail"
```

---

## 3. Post-Fix Verification

With all three targeted modifications applied, re-executing `test_student_utils.py` yields:
```text
Ran 9 tests in 0.000s
OK
```
All unit tests pass without modifying the original test assertions.
