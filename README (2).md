# Even and Odd Number Checker

## Description
A simple Python program that accepts a number from the user and determines whether it is even or odd.

## Objective
Practice conditional statements (`if`/`else`) and the modulus (`%`) operator.

## Tools Used
- Python 3

## How It Works
The program uses the modulus operator (`%`) to check the remainder when the input number is divided by 2.
- If `number % 2 == 0`, the number is **even**.
- Otherwise, the number is **odd**.

Python's `%` operator handles negative numbers correctly out of the box (e.g. `-4 % 2 == 0`, `-3 % 2 == 1`), so no extra logic is needed for negative inputs.

## Deliverables

### Python Program
See [`even_odd_checker.py`](./even_odd_checker.py).

### Example Outputs
```
8 is Even.
7 is Odd.
-4 is Even.
-3 is Odd.
0 is Even.

Enter a number: 15
15 is Odd.
```

## How to Run
```bash
python3 even_odd_checker.py
```
The script first prints a few example runs (including negative numbers and zero), then prompts you to enter your own number.

## Interview Questions & Answers

**1. How do you check whether a number is even in Python?**
Use the modulus operator: `number % 2 == 0`. This checks if there's no remainder when dividing by 2, which means the number is even.

**2. What is the purpose of the `%` operator?**
It returns the remainder of a division. It's commonly used for checking divisibility (like even/odd checks), cycling values within a range, and extracting digits from numbers.

**3. What is the difference between `if`, `elif`, and `else`?**
- `if` evaluates a condition and executes its block if the condition is `True`.
- `elif` (short for "else if") is checked only if the previous `if`/`elif` conditions were `False`, allowing multiple conditions to be chained.
- `else` runs when none of the preceding `if`/`elif` conditions were true, and takes no condition of its own.

## Outcome
The program was completed successfully and tested with even, odd, negative, and zero inputs to confirm correct behavior in all cases.
