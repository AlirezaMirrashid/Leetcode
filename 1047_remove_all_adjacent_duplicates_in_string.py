"""
🔵 LeetCode 1047: Remove All Adjacent Duplicates in String

You are given a string `s` consisting of lowercase English letters. A duplicate removal consists of choosing 
two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on `s` until we can no longer make any removals.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

-----------------------------------
Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation:
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only 
    possible move. The result of this move is that the string is "aaca", of which only "aa" is possible, so the 
    final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"

-----------------------------------

Constraints:
    - 1 <= s.length <= 10^5
    - s consists of lowercase English letters.
"""

def removeDuplicates(s: str) -> str:
    """
    This function removes all adjacent duplicate characters from the string `s` until no more adjacent duplicates
    remain. The process continues until there are no further adjacent duplicate pairs to remove.

    Args:
        s (str): The input string from which adjacent duplicates need to be removed.
    
    Returns:
        str: The string after all adjacent duplicate characters have been removed.
    """
    
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If the stack is not empty and the top element is equal to the current character
        if stack and stack[-1] == char:
            # Pop the top element from the stack (this removes the adjacent duplicate)
            stack.pop()
        else:
            # Otherwise, push the current character onto the stack
            stack.append(char)
    
    # Join the stack to form the resulting string
    return ''.join(stack)


# Sample Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abbaca"
    print(removeDuplicates(s1))  # Expected: "ca"
    
    # Test Case 2
    s2 = "azxxzy"
    print(removeDuplicates(s2))  # Expected: "ay"
    
    # Test Case 3 (No duplicates)
    s3 = "abcdef"
    print(removeDuplicates(s3))  # Expected: "abcdef"
    
    # Test Case 4 (All characters are the same)
    s4 = "aaaaaa"
    print(removeDuplicates(s4))  # Expected: ""
    
    # Test Case 5 (Single character)
    s5 = "a"
    print(removeDuplicates(s5))  # Expected: "a"

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the length of the input string `s`. We make one pass through the string.
# ✅ Space Complexity: O(n), where n is the length of the string `s`, as we use a stack to store the characters.
