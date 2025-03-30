"""
🔵 LeetCode 2667: Create Hello World Function

You are tasked with writing a function `createHelloWorld` that returns another function. 
The returned function, when invoked, should always return the string "Hello World", 
no matter what arguments are passed to it.

-----------------------------------
Example 1:
Input: args = []
Output: "Hello World"
Explanation: 
    f = createHelloWorld()
    f()  # "Hello World"

Example 2:
Input: args = [{}, null, 42]
Output: "Hello World"
Explanation:
    f = createHelloWorld()
    f({}, None, 42)  # "Hello World"

-----------------------------------

Constraints:
    - 0 <= args.length <= 10
"""

def createHelloWorld():
    """
    This function returns another function that always returns "Hello World"
    
    The returned function ignores any arguments passed to it and simply returns "Hello World"
    
    Returns:
        function: A function that returns the string "Hello World".
    """
    # Return a function that ignores arguments and always returns "Hello World"
    def hello_world(*args):
        return "Hello World"
    
    return hello_world


# Sample Test Cases
if __name__ == "__main__":
    f = createHelloWorld()
    print(f())  # Expected: "Hello World"
    print(f({}, None, 42))  # Expected: "Hello World"
    
# ------------------------------------------------
# ✅ Time Complexity: O(1), as we are simply returning the string "Hello World" for any call.
# ✅ Space Complexity: O(1), the function does not utilize additional space apart from returning a simple string.
