# LeetCode 227: Basic Calculator II
# Problem Link: https://leetcode.com/problems/basic-calculator-ii/
#
# Description:
# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
# Example 1:
# Input: s = "3+2*2"
# Output: 7
#
# Example 2:
# Input: s = " 3/2 "
# Output: 1
#
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
#
# Constraints:
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.


def basic_calculator(expression: str) -> int:
    """
    Evaluate a basic arithmetic expression given as a string.

    The expression contains non-negative integers and the operators '+', '-', '*', and '/'.
    Division is performed as integer division, truncating toward zero.
    The input expression is assumed to be valid and may contain spaces.

    Parameters:
        expression (str): A string representing a valid arithmetic expression.

    Returns:
        int: The result of evaluating the expression.

    Examples:
        >>> basic_calculator("3+2*2")
        7
        >>> basic_calculator(" 3/2 ")
        1
        >>> basic_calculator(" 3+5 / 2 ")
        5
    """
    index = 0
    current_number = 0
    previous_operand = 0
    result = 0
    current_operator = '+'

    while index < len(expression):
        char = expression[index]
        if char.isdigit():
            # Build the current number from consecutive digits.
            while index < len(expression) and expression[index].isdigit():
                current_number = current_number * 10 + int(expression[index])
                index += 1
            # Adjust index to re-process the non-digit character.
            index -= 1

            # Apply the last seen operator to the current number.
            if current_operator == '+':
                result += current_number
                previous_operand = current_number
            elif current_operator == '-':
                result -= current_number
                previous_operand = -current_number
            elif current_operator == '*':
                result -= previous_operand
                product = previous_operand * current_number
                result += product
                previous_operand = product
            elif current_operator == '/':
                result -= previous_operand
                # Integer division truncates toward zero.
                division_result = int(previous_operand / current_number)
                result += division_result
                previous_operand = division_result

            # Reset current number for the next iteration.
            current_number = 0
        elif char != ' ':
            # Update the operator when encountering a non-digit non-space character.
            current_operator = char
        index += 1

    return result


# Example test cases:
if __name__ == "__main__":
    print(basic_calculator("3+2*2"))       # Expected output: 7
    print(basic_calculator(" 3/2 "))       # Expected output: 1
    print(basic_calculator(" 3+5 / 2 "))    # Expected output: 5
    print(basic_calculator("12+34-1*12/3")) # Expected output: 42
    print(basic_calculator("-12+34")) # Expected output: 22
