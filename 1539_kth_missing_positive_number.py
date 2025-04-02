"""
🔵 LeetCode 1539: Kth Missing Positive Number

Given an array `arr` of positive integers sorted in strictly increasing order, and an integer `k`,
return the kth positive integer that is missing from this array.

-----------------------------------
Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

-----------------------------------
Constraints:
    - 1 <= arr.length <= 1000
    - 1 <= arr[i] <= 1000
    - 1 <= k <= 1000
    - arr[i] < arr[j] for 1 <= i < j <= arr.length

Follow up:
    Could you solve this problem in less than O(n) complexity?
"""

from typing import List
import bisect

# ------------------------------
# Approach 1: Linear Scan
# ------------------------------
def findKthMissing_linear(arr: List[int], k: int) -> int:
    """
    This function finds the kth missing positive integer using a linear scan.
    
    Approach:
      - Initialize a counter for missing numbers and a variable for the current number.
      - Iterate starting from 1 and compare with the array elements.
      - Increase the missing counter when a number is not found in the array.
      - When the missing count equals k, return that number.
    
    
    Args:
        arr (List[int]): A sorted list of positive integers.
        k (int): The kth missing number to find.
    
    Returns:
        int: The kth missing positive integer.
    """
    missing = 0
    current = 1
    i = 0
    n = len(arr)
    
    while missing < k:
        if i < n and arr[i] == current:
            i += 1
        else:
            missing += 1
            if missing == k:
                return current
        current += 1
    return current  # This line is theoretically unreachable

# ------------------------------
# Approach 2: Binary Search
# ------------------------------
def findKthMissing_binary(arr: List[int], k: int) -> int:
    """
    Finds the kth missing positive integer using binary search.
    
    Key Observation:
      - For any index i, the number of missing numbers before arr[i] is:
            missing(i) = arr[i] - i - 1
      - Use binary search to find the smallest index such that missing(i) >= k.
    
    If such an index is found:
      - The kth missing number is: arr[index-1] + (k - missing(index-1))
    Otherwise, if k is larger than the missing count before the last element:
      - The kth missing number is: arr[-1] + (k - (arr[-1] - len(arr)))

    
    Args:
        arr (List[int]): A sorted list of positive integers.
        k (int): The kth missing number to find.
    
    Returns:
        int: The kth missing positive integer.
    """
    n = len(arr)
    left, right = 0, n
    
    # Binary search: find the first index where missing numbers >= k
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] - mid - 1 < k:
            left = mid + 1
        else:
            right = mid
    
    # If left is 0, then kth missing is simply k (when k < arr[0])
    if left == 0:
        return k
    # Otherwise, kth missing lies between arr[left-1] and arr[left] (or beyond arr[-1])
    missing_before = arr[left - 1] - (left - 1) - 1
    return arr[left - 1] + (k - missing_before)

# ------------------------------
# Approach 3: Linear Search
# ------------------------------

def findKthMissing_alternative(arr: List[int], k: int) -> int:
    """
    Alternative Approach Using a While/For Loop to Compare k with Gaps in the Array
    
    Approach:
      - Initialize a variable `prev` to 0 (representing the number before the first positive integer).
      - Iterate through each number in `arr` and calculate the missing numbers between `prev` and the current number:
            missing = current number - prev - 1
      - If k is less than or equal to the missing count, the kth missing number is `prev + k`.
      - Otherwise, subtract the missing count from k and update `prev` to the current number.
      - If k remains after processing all elements, the kth missing number is beyond the last element:
            return arr[-1] + k
      
    Time Complexity: O(n), where n is the length of arr.
    Space Complexity: O(1)
    
    Args:
        arr (List[int]): A sorted list of positive integers.
        k (int): The kth missing positive integer to find.
    
    Returns:
        int: The kth missing positive integer.
    """
    prev = 0
    for num in arr:
        # Number of missing numbers between `prev` and `num`
        missing = num - prev - 1
        if k <= missing:
            return prev + k
        k -= missing
        prev = num
    # If k is still greater than 0, the kth missing number lies after the last element of arr.
    return prev + k

# Sample Test Cases
if __name__ == "__main__":
    # Example 1:
    arr1 = [2, 3, 4, 7, 11]
    k1 = 5
    print("Linear Scan Approach, Example 1 Output:", findKthMissing_linear(arr1, k1))  # Expected: 9
    print("Binary Search Approach, Example 1 Output:", findKthMissing_binary(arr1, k1))  # Expected: 9

    # Example 2:
    arr2 = [1, 2, 3, 4]
    k2 = 2
    print("Linear Scan Approach, Example 2 Output:", findKthMissing_linear(arr2, k2))  # Expected: 6
    print("Binary Search Approach, Example 2 Output:", findKthMissing_binary(arr2, k2))  # Expected: 6

# ------------------------------------------------
# ✅ Time Complexity:
#     - Linear Scan Approach: O(n + k) in the worst-case scenario.
#     - Binary Search Approach: O(log n)
# ✅ Space Complexity: O(1), as only a constant amount of extra space is used.
