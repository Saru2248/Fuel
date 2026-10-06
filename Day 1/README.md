# Python Full Stack Training - Day 1

Beginner-friendly Python programs created to practice fundamental concepts:
- Variables & basic data types
- `input()` and `print()` functions
- Type casting (`int()`, `float()`)
- Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`)
- String formatting with `f-strings`

---

## Programs Overview

### 1. Circle Calculator (`01_circle.py`)
- Takes the radius as user input.
- Calculates the area using `3.14 * radius * radius`.
- Calculates the circumference using `2 * 3.14 * radius`.
- Prints both values using f-strings.

### 2. Sum of Digits (`02_sum_of_digits.py`)
- Takes a 3-digit integer as user input.
- Finds hundreds, tens, and units digits using floor division (`//`) and modulo (`%`).
- Prints the individual digits and their sum.

### 3. Simple Bill Calculator (`03_bill_calculator.py`)
- Takes item price and quantity as user input.
- Computes `subtotal = price * quantity`.
- Adds 18% GST (`subtotal * 0.18`).
- Prints subtotal, GST, and final amount using f-strings.

### 4. Time Converter (`04_time_converter.py`)
- Takes total seconds as user input.
- Converts total seconds into hours, minutes, and remaining seconds using `//` and `%`.
- Prints the result using f-strings.

---

## How to Run

Navigate into the `Day 1` folder and run any program using Python:

```bash
cd "Day 1"
python 01_circle.py
python 02_sum_of_digits.py
python 03_bill_calculator.py
python 04_time_converter.py
```
