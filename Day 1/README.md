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
Calculates and displays the area and circumference of a circle given its radius using $PI = 3.14$.

**Formulas:**
- `Area = 3.14 * radius * radius`
- `Circumference = 2 * 3.14 * radius`

**Example Input & Output:**
```text
Enter the radius of the circle: 5
Radius: 5.0
Area of the circle: 78.5
Circumference of the circle: 31.400000000000002
```

---

### 2. Sum of Digits (`02_sum_of_digits.py`)
Takes a 3-digit integer, extracts the hundreds, tens, and units digits using floor division (`//`) and modulo (`%`), and calculates their sum.

**Example Input & Output:**
```text
Enter a 3-digit number: 123
Hundreds digit: 1
Tens digit: 2
Units digit: 3
Sum of digits (1 + 2 + 3): 6
```

---

### 3. Simple Bill Calculator (`03_bill_calculator.py`)
Takes item price and quantity, computes the subtotal, calculates an 18% GST charge, and prints a formatted bill summary.

**Formulas:**
- `subtotal = price * quantity`
- `gst = subtotal * 0.18`
- `final_amount = subtotal + gst`

**Example Input & Output:**
```text
Enter item price: 150
Enter item quantity: 2

--- Bill Summary ---
Price per item : 150.0
Quantity       : 2
Subtotal       : 300.0
GST (18%)      : 54.0
Final Amount   : 354.0
```

---

### 4. Time Converter (`04_time_converter.py`)
Converts an input in total seconds into hours, minutes, and remaining seconds using `//` and `%`.

**Example Input & Output:**
```text
Enter total seconds: 3670
3670 seconds = 1 hour(s), 1 minute(s), 10 second(s)
```

---

## How to Run

Open your terminal or command prompt in this directory and run any program using Python:

```bash
python 01_circle.py
python 02_sum_of_digits.py
python 03_bill_calculator.py
python 04_time_converter.py
```

