"""
🔵 LeetCode 163: Missing Ranges

Given a sorted integer array `nums`, where the range of elements are in the inclusive range [lower, upper],
return its missing ranges.

-----------------------------------
Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99
Output: ["2", "4->49", "51->74", "76->99"]
Explanation:
    The missing positive integers in the range are:
      - "2" is missing between 1 and 3.
      - "4->49" is missing between 3 and 50.
      - "51->74" is missing between 50 and 75.
      - "76->99" is missing between 75 and 99.
      
-----------------------------------
Constraints:
    - The array `nums` is sorted in ascending order.
    - `lower` and `upper` are integers that define the inclusive range.
"""

from typing import List

def missingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    """
    Returns a list of missing ranges within the inclusive interval [lower, upper] that are not present in the sorted array nums.
    
    Approach:
      - Initialize a variable `prev` to lower - 1 to handle the beginning of the range.
      - Append (upper + 1) to nums to handle the final range.
      - Iterate through the modified array and for each element, compute the gap between the current element and `prev`.
      - If the gap equals 2, then only one number is missing; append that number as a string.
      - If the gap is greater than 2, then a range of numbers is missing; append the range in the format "start->end".
      - Update `prev` to the current element.
    
    Time Complexity: O(n), where n is the length of nums.
    Space Complexity: O(1) (excluding the space used for the output list).
    
    Args:
        nums (List[int]): Sorted list of integers.
        lower (int): The lower bound of the range (inclusive).
        upper (int): The upper bound of the range (inclusive).
    
    Returns:
        List[str]: A list of missing ranges as strings.
    """
    res = []
    prev = lower - 1  # Initialize previous number to one less than lower
    
    # Append upper + 1 to cover the range end
    for num in nums + [upper + 1]:
        # If there's exactly one missing number between prev and num
        if num - prev == 2:
            res.append(str(prev + 1))
        # If more than one missing number, add the range
        elif num - prev > 2:
            res.append(f"{prev + 1}->{num - 1}")
        prev = num
    
    return res

# Sample Test Cases
if __name__ == "__main__":
    # Example:
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print("Example Output:", missingRanges(nums, lower, upper))
    # Expected: ["2", "4->49", "51->74", "76->99"]

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the length of the array nums.
# ✅ Space Complexity: O(1), excluding the space for the output list.
