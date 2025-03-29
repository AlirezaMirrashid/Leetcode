"""
🔵 LeetCode 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.

-----------------------------------
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

-----------------------------------
Constraints:
    - 1 <= s.length <= 10^4
    - s consists of parentheses only '()[]{}'.
"""

def is_valid_parentheses_stack(s: str) -> bool:
    """
    ✅ Optimal Solution Using a Stack

    Approach:
      - Use a stack to keep track of open brackets.
      - For every character in the string:
          - If it is an open bracket, push it onto the stack.
          - If it is a close bracket, check if the stack is not empty and
            the top element of the stack is the corresponding open bracket.
            If yes, pop from the stack; otherwise, return False.
      - If the stack is empty at the end, the string is valid.

    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(n) in the worst-case scenario.
    """
    # Mapping of closing brackets to their corresponding opening brackets.
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map.values():
            # If the character is an opening bracket, push it onto the stack.
            stack.append(char)
        elif char in bracket_map:
            # If the character is a closing bracket, check for its corresponding opening bracket.
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            # In case the character is not one of the expected ones.
            return False
    
    return not stack


def is_valid_parentheses_bruteforce(s: str) -> bool:
    """
    ❌ Brute-Force (Iterative Removal) Approach

    Approach:
      - Iteratively remove pairs of valid adjacent parentheses "()", "{}", and "[]"
        from the string until no more can be removed.
      - If the string becomes empty, it is valid; otherwise, it is invalid.

    Time Complexity: O(n^2) in the worst case due to repeated scanning.
    Space Complexity: O(n) for string manipulation.
    """
    prev_length = -1
    while prev_length != len(s):
        prev_length = len(s)
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""


# Sample Test Cases
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("", True),  # Edge case: empty string
        ("{[]}", True)
    ]
    
    print("Testing Optimal Stack Approach:")
    for s, expected in test_cases:
        result = is_valid_parentheses_stack(s)
        print(f"Input: {s:10} Expected: {expected}  Got: {result}")
    
    print("\nTesting Brute-Force Iterative Removal Approach:")
    for s, expected in test_cases:
        result = is_valid_parentheses_bruteforce(s)
        print(f"Input: {s:10} Expected: {expected}  Got: {result}")
