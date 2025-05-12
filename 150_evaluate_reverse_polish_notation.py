"""
🔵 LeetCode 150. Evaluate Reverse Polish Notation

You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation (RPN).

Return the evaluated result as an integer.

Rules:
- The valid operators are '+', '-', '*', and '/'.
- Operands are integers.
- Division truncates toward zero.
- The input is a valid RPN expression.

-----------------------------------
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22

-----------------------------------
Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200]
"""

from typing import List

def eval_rpn(tokens: List[str]) -> int:
    """
    ✅ Stack-based Evaluation

    Idea:
    - Use a stack to evaluate expressions in RPN.
    - Push operands to the stack.
    - When an operator is encountered, pop two operands, apply the operation, push result back.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                res = a + b
            elif token == "-":
                res = a - b
            elif token == "*":
                res = a * b
            else:  # division
                res = int(a / b)  # truncate toward zero
            stack.append(res)
        else:
            stack.append(int(token))
    return stack[0]


# ✅ Sample Test Cases
if __name__ == "__main__":
    tokens1 = ["2","1","+","3","*"]
    print(eval_rpn(tokens1))  # Output: 9

    tokens2 = ["4","13","5","/","+"]
    print(eval_rpn(tokens2))  # Output: 6

    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(eval_rpn(tokens3))  # Output: 22
