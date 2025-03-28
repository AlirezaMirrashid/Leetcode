# LeetCode 346: Moving Average from Data Stream
# Problem Link: https://leetcode.com/problems/moving-average-from-data-stream/
#
# Description:
# Given a stream of integers and a window size, calculate the moving average of 
# all integers in the sliding window.
#
# Implement the MovingAverage class:
# - MovingAverage(int size): Initializes the object with the size of the window.
# - double next(int val): Returns the moving average of the last `size` values 
#   of the stream.
#
# Example:
#
# Input:
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
#
# Output:
# [null, 1.0, 5.5, 4.66667, 6.0]
#
# Explanation:
# MovingAverage movingAverage = MovingAverage(3);
# movingAverage.next(1);  # return 1.0 = 1 / 1
# movingAverage.next(10); # return 5.5 = (1 + 10) / 2
# movingAverage.next(3);  # return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5);  # return 6.0 = (10 + 3 + 5) / 3
#
# Constraints:
# 1 <= size <= 1000
# -10^5 <= val <= 10^5
# At most 10^4 calls will be made to next.

from collections import deque

class MovingAverage:
    """
    Class to calculate the moving average of the last `size` values in a stream.
    """

    def __init__(self, size: int):
        """
        Initializes the data structure with a fixed window size.

        Parameters:
            size (int): The maximum number of elements to consider in the moving average.
        """
        self.size = size
        self.queue = deque()  # Queue to store the last 'size' values
        self.window_sum = 0  # Sum of elements in the current window

    def next(self, val: int) -> float:
        """
        Adds a new value to the stream and returns the updated moving average.

        Parameters:
            val (int): The new integer value from the stream.

        Returns:
            float: The moving average of the last `size` values.
        """
        self.queue.append(val)
        self.window_sum += val

        # If the queue exceeds the allowed size, remove the oldest element
        if len(self.queue) > self.size:
            self.window_sum -= self.queue.popleft()

        # Compute the moving average
        return self.window_sum / len(self.queue)


# Example test cases:
movingAverage = MovingAverage(3)
print(movingAverage.next(1))   # Expected output: 1.0
print(movingAverage.next(10))  # Expected output: 5.5
print(movingAverage.next(3))   # Expected output: 4.66667
print(movingAverage.next(5))   # Expected output: 6.0

# Complexity Analysis:
# Time Complexity: 
# O(1)
# O(1) for each next operation since deque operations (append and popleft) are O(1)

# Space Complexity: 
# O(size)
# O(size) since we store only size elements in the queue.