"""
Leetcode 56. Merge Intervals
Medium
Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""




from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges overlapping intervals from the input list.

    This function first sorts the intervals based on their starting times.
    Then, it iterates over the sorted list and merges intervals that overlap.
    Two intervals [a, b] and [c, d] overlap if c <= b. When they overlap, they are merged into
    a new interval [a, max(b, d)].

    Parameters:
        intervals (List[List[int]]): A list of intervals where each interval is represented as [start, end].

    Returns:
        List[List[int]]: A list of the merged non-overlapping intervals that cover all the intervals in the input.
    """
    if not intervals:
        return []

    # Sort intervals based on their start time.
    intervals.sort(key=lambda x: x[0])

    merged = []
    # Initialize the current interval as the first interval.
    current_interval = intervals[0]

    for next_interval in intervals[1:]:
        # If the next interval overlaps with the current interval, merge them.
        if next_interval[0] <= current_interval[1]:
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            # No overlap: add the current interval to the merged list and update the current interval.
            merged.append(current_interval)
            current_interval = next_interval

    # Append the final interval.
    merged.append(current_interval)
    return merged


def merge_intervals_bruteforce(intervals: List[List[int]]) -> List[List[int]]:
    """
    Brute-force approach to merge overlapping intervals.
    
    This method repeatedly scans through the list of intervals and merges any pair
    of intervals that overlap. The process repeats until no more intervals can be merged.
    
    Parameters:
        intervals (List[List[int]]): A list of intervals represented as [start, end].
    
    Returns:
        List[List[int]]: The list of merged, non-overlapping intervals.
        
    Time Complexity:
        O(n^2) in the worst case, since we may need to compare many pairs of intervals 
        repeatedly until no more merges occur.
        
    Space Complexity:
        O(n) for storing the merged intervals.
    """
    if not intervals:
        return []
    
    merged = intervals[:]  # Work on a copy of the list
    changed = True

    while changed:
        changed = False
        new_merged = []
        used = [False] * len(merged)
        i = 0
        # Sort intervals to make merging easier (by start time)
        merged.sort(key=lambda x: x[0])
        
        while i < len(merged):
            # Start with the current interval
            current = merged[i]
            j = i + 1
            # Try to merge with subsequent intervals if overlapping
            while j < len(merged):
                next_interval = merged[j]
                # If the next interval overlaps with the current one
                if next_interval[0] <= current[1]:
                    current = [current[0], max(current[1], next_interval[1])]
                    changed = True
                    j += 1
                else:
                    break
            new_merged.append(current)
            i = j  # Move to the next non-merged interval
        
        merged = new_merged  # Update merged with new list of intervals

    return merged

# Example test cases:
if __name__ == "__main__":
    # Example 1:
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("Merged Intervals (Example 1):", merge_intervals(intervals1))
    # Expected output: [[1,6],[8,10],[15,18]]

    # Example 2:
    intervals2 = [[1, 4], [4, 5]]
    print("Merged Intervals (Example 2):", merge_intervals(intervals2))
    # Expected output: [[1,5]]


# Time and Space Complexity Analysis:
#
# Time Complexity:
#   - Sorting the intervals takes O(n log n), where n is the number of intervals.
#   - Merging intervals takes O(n) in a single pass.
#   Overall: O(n log n)
#
# Space Complexity:
#   - O(n) is used to store the merged intervals.
