# LeetCode 1249: Minimum Remove to Make Valid Parentheses
# Problem Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

def min_remove_to_make_valid(s: str) -> str:
    # Step 1: First pass - remove excess closing parentheses
    res = []  # This will store characters as we build the intermediate valid string
    open_count = 0  # Variable to keep track of unmatched opening parentheses '('

    # Iterate through the string to handle closing parentheses ')'
    for char in s:
        if char == '(':
            # If it's an opening parenthesis, increment open_count and add it to the result
            open_count += 1
            res.append(char)
        elif char == ')' and open_count > 0:
            # If it's a closing parenthesis and we have an unmatched '(' (open_count > 0)
            open_count -= 1  # Match the ')' with the '('
            res.append(char)  # Add the valid closing parenthesis to the result
        elif char != ')':
            # If it's neither '(' nor ')', just add it directly to the result list
            res.append(char)

    # Step 2: Second pass - remove excess opening parentheses
    # At this point, `res` contains the string with excess closing parentheses removed.
    result = []  # This will store the final valid string (reversed order)

    # Traverse the result list in reverse order to remove any unmatched '('
    for char in reversed(res):
        if char == '(' and open_count > 0:
            # If we encounter an unmatched '(', decrement open_count and skip it
            open_count -= 1
        else:
            # If it's a valid character, append it to the result list
            result.append(char)

    # Return the final valid string, reversing the result list back to correct order
    return ''.join(reversed(result))


# Example test cases
print(min_remove_to_make_valid("lee(t(c)o)de)"))  # Output: "lee(t(c)o)de"
print(min_remove_to_make_valid("a)b(c)d"))  # Output: "ab(c)d"
print(min_remove_to_make_valid("))(("))  # Output: ""

# Time and Space Complexity Analysis:
# Time Complexity: O(n)
# - We make two passes over the string: one to handle closing parentheses and one to handle opening parentheses.
# - Since each pass processes each character in the string once, the time complexity is O(n), where n is the length of the string.

# Space Complexity: O(n)
# - We use two additional lists (`res` and `result`) to store intermediate and final results, both of which can store up to n characters.
# - Therefore, the space complexity is O(n), where n is the length of the string.
