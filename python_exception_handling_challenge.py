"""
Exercise: Python Exception Handling Challenge (id=101)

* Tests for the function are included. Run this script to test your function.
* To just try your function witout running the tests, uncomment your function from the "if __name__ = '__main__':" block.


Requirements:

Write a Python function divide_numbers(num1, num2) that performs division on two integers and handles exceptions gracefully.
Your function should adhere to the following requirements:

The function should take two integer arguments, num1 and num2.
If either num1 or num2 is not an integer, your function should raise a ValueError with the message "Invalid input. Please enter integers."
If num2 is zero, your function should raise a ZeroDivisionError with the message "Division by zero is not allowed."
If any other exception occurs during the division operation, your function should return a generic error message "An error occurred."
If the division is successful, your function should return the result as a float.

Instructions:
Your task is to implement the divide_numbers function according to the specified requirements. Make sure to handle exceptions as described and return the appropriate messages or results.
Please test your function with various input scenarios, including valid division, division by zero, and invalid input.

Examples:

Here are some examples to illustrate the expected behavior of your function:

Valid Division:

Input: divide_numbers(8, 4)
Expected Output: 2.0
Explanation: The function should successfully divide 8 by 4, returning in 2.0.

Division by Zero:
Input: divide_numbers(10, 0)
Expected Output: "Division by zero is not allowed."
Explanation: The function should raise a ZeroDivisionError and return the specified error message.

Invalid Input (Non-Integer):
Input: divide_numbers("5", 2)
Expected Output: "Invalid input. Please enter integers."
Explanation: The function should raise a ValueError and return the specified error message due to the non-integer input.

Generic Error:
Input: divide_numbers(6, 2.5)
Expected Output: "An error occurred."
Explanation: The function should encounter a non-integer input and return the generic error message.

"""


import unittest

def divide_numbers(num1, num2):

    try:
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Invalid input. Please enter integers.")
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return float(num1/num2)
    except ValueError as ve:
        return str(ve)
    except ZeroDivisionError as ze:
        return str(ze)
    except Exception as e:
        return "An error occurred."








#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
class TestDivideNumbers(unittest.TestCase):

    def test_valid_division(self):
        """
        Test that the function correctly divides two integers.
        """
        self.assertEqual(divide_numbers(4, 2), 2.0)

    def test_divide_by_zero(self):
        """
        Test that division by zero raises a ZeroDivisionError.
        """
        self.assertEqual(divide_numbers(4, 0), "Division by zero is not allowed.")

    def test_invalid_input1(self):
        """
        Test that non-integer input raises a ValueError.
        """
        self.assertEqual(divide_numbers(4.5, 2), "Invalid input. Please enter integers.")

    def test_invalid_input2(self):
        """
        Test that non-integer input raises a ValueError.
        """
        self.assertEqual(divide_numbers("4", 2), "Invalid input. Please enter integers.")

    def test_invalid_input3(self):
        """
        Test that non-integer input raises a ValueError.
        """
        self.assertEqual(divide_numbers(4, "2"), "Invalid input. Please enter integers.")

if __name__ == "__main__":
    unittest.main()

    #divide_numbers(6, 2.5)
