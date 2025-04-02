"""
🔵 LeetCode 70: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

-----------------------------------
Example 1:
Input: n = 2
Output: 2
Explanation:
    There are two ways to climb to the top:
      1. 1 step + 1 step
      2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation:
    There are three ways to climb to the top:
      1. 1 step + 1 step + 1 step
      2. 1 step + 2 steps
      3. 2 steps + 1 step

-----------------------------------
Constraints:
    - 1 <= n <= 45
"""

def climbStairs(n: int) -> int:
    """
    This function returns the number of distinct ways to climb a staircase of n steps,
    where each move can either be 1 step or 2 steps.
    
    Approach:
      - The problem is equivalent to computing the Fibonacci sequence:
            - For 1 step, there is 1 way: [1]
            - For 2 steps, there are 2 ways: [1,1] or [2]
            - For n > 2, the number of ways to climb n steps is the sum of ways to climb n-1 steps 
              and n-2 steps, because from step n-1 you take one step, and from step n-2 you take two steps.
      - We compute this iteratively using two variables to save space.
    
    Time Complexity: O(n), where n is the number of steps.
    Space Complexity: O(1), since only a constant amount of extra space is used.
    
    Args:
        n (int): The total number of steps to climb.
    
    Returns:
        int: The number of distinct ways to reach the top.
    """
    if n <= 1:
        return 1

    # Initialize base cases:
    first, second = 1, 2  # ways to climb 1 step and 2 steps respectively
    
    if n == 1:
        return first
    elif n == 2:
        return second
    
    # Compute the number of ways for each step from 3 to n
    for _ in range(3, n + 1):
        first, second = second, first + second
        
    return second

# Sample Test Cases
if __name__ == "__main__":
    print("Example 1 Output:", climbStairs(2))  # Expected: 2
    print("Example 2 Output:", climbStairs(3))  # Expected: 3

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the number of steps.
# ✅ Space Complexity: O(1), since only a constant amount of extra space is used.
