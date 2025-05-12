"""
🔵 LeetCode 346: Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

-----------------------------------
Example:
Input: 
    MovingAverage m = new MovingAverage(3);
    m.next(1)  -> 1
    m.next(10) -> (1 + 10) / 2 = 5.5
    m.next(3)  -> (1 + 10 + 3) / 3 = 4.67
    m.next(5)  -> (10 + 3 + 5) / 3 = 6
Output:
    [1, 5.5, 4.67, 6]

-----------------------------------

Constraints:
    - 1 <= size <= 1000
    - -10⁵ <= val <= 10⁵
    - At most 10⁴ calls will be made to next(val).
"""

from collections import deque

class MovingAverage:
    """
    A class that calculates the moving average of the last 'size' elements in a stream.
    
    Attributes:
        size (int): The window size for the moving average.
        queue (deque): A queue storing the last 'size' elements.
        total (float): The sum of the elements in the queue.
    
    Methods:
        next(val): Adds a new number to the stream and returns the updated moving average.
    
    Time Complexity: O(1) for each call to next(val).
    Space Complexity: O(size) for storing the sliding window.
    """
    
    def __init__(self, size: int):
        """Initializes the MovingAverage class with a given window size."""
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        """
        Adds a new integer to the stream and returns the updated moving average.
        
        Args:
            val (int): The new value to be added.
        
        Returns:
            float: The updated moving average.
        """
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        
        return self.total / len(self.queue)


# Sample Test Cases
if __name__ == "__main__":
    m = MovingAverage(3)
    print(m.next(1))   # Expected: 1
    print(m.next(10))  # Expected: 5.5
    print(m.next(3))   # Expected: 4.67
    print(m.next(5))   # Expected: 6.0

# ------------------------------------------------
# ✅ Time Complexity: O(1) per call to next()
# ✅ Space Complexity: O(size), as we maintain a fixed sliding window.
