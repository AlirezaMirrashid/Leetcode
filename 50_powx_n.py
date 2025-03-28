"""
LeetCode 50: Pow(x, n)
Problem Link: https://leetcode.com/problems/powx-n/

Description:
    Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

    Example 1:
        Input:  x = 2.00000, n = 10
        Output: 1024.00000

    Example 2:
        Input:  x = 2.10000, n = 3
        Output: 9.26100

    Example 3:
        Input:  x = 2.00000, n = -2
        Output: 0.25000
        Explanation: 2^-2 = 1 / 2^2 = 1/4 = 0.25

Constraints:
    -100.0 < x < 100.0
    -2^31 <= n <= 2^31 - 1
    n is an integer.
    Either x is not zero or n > 0.
    -10^4 <= x^n <= 10^4

This module implements two approaches to solve the problem:
    1. Iterative solution using exponentiation by squaring.
    2. Recursive solution using exponentiation by squaring.
"""

def myPow_iterative(x: float, n: int) -> float:
    """
    Computes x raised to the power n using an iterative approach
    with exponentiation by squaring.
    
    Parameters:
        x (float): The base value.
        n (int): The exponent value (can be negative).
    
    Returns:
        float: The result of x raised to the power n.
    """
    # Handle negative exponent by taking the reciprocal later.
    N = abs(n)
    result = 1.0
    current_product = x
    
    while N:
        # If current bit is set, multiply result by the current product.
        if N & 1:
            result *= current_product
        # Square the current product for the next bit.
        current_product *= current_product
        # Shift N right by 1 bit (i.e., integer division by 2).
        N >>= 1
    
    return result if n >= 0 else 1.0 / result


def myPow_recursive(x: float, n: int) -> float:
    """
    Computes x raised to the power n using a recursive approach
    with exponentiation by squaring.
    
    Parameters:
        x (float): The base value.
        n (int): The exponent value (can be negative).
    
    Returns:
        float: The result of x raised to the power n.
    """
    def rec_power(base: float, exp: int) -> float:
        # Base case: any number raised to the power 0 is 1.
        if exp == 0:
            return 1.0
        # Recursively compute half power.
        half = rec_power(base, exp // 2)
        # If exp is even, simply square the half power.
        if exp % 2 == 0:
            return half * half
        else:
            # If exp is odd, multiply an extra base.
            return half * half * base

    # If exponent is negative, compute power with positive exponent and take reciprocal.
    if n < 0:
        return 1.0 / rec_power(x, -n)
    else:
        return rec_power(x, n)


# Example test cases:
if __name__ == "__main__":
    # Test iterative solution:
    print("Iterative Approach:")
    print(f"myPow_iterative(2.00000, 10) = {myPow_iterative(2.00000, 10)}")  # Expected: 1024.00000
    print(f"myPow_iterative(2.10000, 3) = {myPow_iterative(2.10000, 3)}")    # Expected: 9.26100
    print(f"myPow_iterative(2.00000, -2) = {myPow_iterative(2.00000, -2)}")  # Expected: 0.25000

    # Test recursive solution:
    print("\nRecursive Approach:")
    print(f"myPow_recursive(2.00000, 10) = {myPow_recursive(2.00000, 10)}")  # Expected: 1024.00000
    print(f"myPow_recursive(2.10000, 3) = {myPow_recursive(2.10000, 3)}")    # Expected: 9.26100
    print(f"myPow_recursive(2.00000, -2) = {myPow_recursive(2.00000, -2)}")  # Expected: 0.25000

# Time and Space Complexity Analysis:
#
# Both approaches implement exponentiation by squaring.
#
# Time Complexity:
#   O(log |n|) for both the iterative and recursive methods,
#   because the exponent is halved at each step.
#
# Space Complexity:
#   Iterative Approach: O(1)
#   Recursive Approach: O(log |n|) due to recursion stack depth.
