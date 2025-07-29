A simple Python program that validates secret codes (strings of digits) against advanced rules. It checks alternation of even/odd digits, uniqueness of digits, a middle-digit rule, and prime boundaries. It prints a clear reason when a rule is violated and returns True or False for integration.

Validation Rules

1. Even–Odd Alternation: Adjacent digits must alternate between even and odd.


2. Unique Digits: All digits must be unique (no repeats).


3. Middle Rule:

Odd length: the middle digit must be greater than 4.

Even length: the average of the two middle digits must be greater than 4.



4. Prime Boundaries: The first and last digits must be prime numbers from {2, 3, 5, 7}.



Example

Enter digits (e.g., 2583): 32547
Success! All checks passed.
True

Enter digits (e.g., 2583): 2245
Error: All digits must be unique
False

How It Works (high level)

Reads an input like "32547".

Converts the string into a list of integer digits.

Runs each rule; on the first failure it prints the reason and returns False.

If all checks pass, it prints a success message and returns True. secret_code_analyzer.py

Run Locally

Requirements: Python 3.x

In the project folder, run:

Windows:

py -3 secret_code_analyzer.py or python secret_code_analyzer.py


macOS/Linux:

python3 secret_code_analyzer.py




When prompted, enter a string of digits (e.g., 32547).

Notes

Input must be digits only (0–9).

If you want the program to return a message instead of printing, you can refactor the function to return strings like "Pattern Accepted" or "Pattern Rejected – <reason>".


Future Improvements

Unit tests for each rule.

Command-line flags (e.g., --quiet, --json).

GUI or web interface.

Package and publish to PyPI
