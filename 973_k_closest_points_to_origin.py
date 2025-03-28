"""

LeetCode 973: K Closest Points to Origin
Problem Link: https://leetcode.com/problems/k-closest-points-to-origin/

Description:
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and 
    an integer k, return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance 
    (i.e., √((x1 - x2)^2 + (y1 - y2)^2)). You may return the answer in any order. 
    The answer is guaranteed to be unique (except for the order that it is in).

Examples:
    Example 1:
        Input: points = [[1,3],[-2,2]], k = 1
        Output: [[-2,2]]
        Explanation:
            Distance from (1,3) to (0,0) = sqrt(1^2 + 3^2) = sqrt(10)
            Distance from (-2,2) to (0,0) = sqrt((-2)^2 + 2^2) = sqrt(8)
            Since sqrt(8) < sqrt(10), (-2,2) is closer to the origin.

    Example 2:
        Input: points = [[3,3],[5,-1],[-2,4]], k = 2
        Output: [[3,3],[-2,4]]
        Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
    - 1 <= k <= points.length <= 10^4
    - -10^4 <= xi, yi <= 10^4
"""


import heapq
import math
from typing import List

def k_closest_points_to_origin(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Returns the k closest points to the origin (0, 0) using a heap-based approach.

    This function maintains a max-heap of size k (by storing negative distances) to keep track of
    the k closest points. For each point, it computes the Euclidean distance to the origin. If the
    heap has fewer than k elements, the point is pushed onto the heap. Otherwise, if the current
    point is closer than the farthest point in the heap, it replaces the farthest point.

    Parameters:
        points (List[List[int]]): A list of points, where each point is represented as [x, y].
        k (int): The number of closest points to return.

    Returns:
        List[List[int]]: A list of the k closest points to the origin.
    """
    # If the number of points is less than or equal to k, return all points.
    if len(points) <= k:
        return points

    # Initialize a max-heap (using negative distances) of size k.
    max_heap = []
    
    for point in points:
        # Calculate the Euclidean distance from the origin.
        dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
        
        # If the heap has fewer than k elements, push the current point.
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-dist, point))
        else:
            # Compare the current point's distance with the farthest point in the heap.
            if -max_heap[0][0] > dist:
                # Remove the farthest point and push the current point.
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-dist, point))

    # Extract the points from the heap.
    return [point for (_, point) in max_heap]


# Example test cases:
if __name__ == "__main__":
    # Example 1:
    points1 = [[1, 3], [-2, 2]]
    k1 = 1
    print("Example 1 Output:", k_closest_points_to_origin(points1, k1))
    # Expected output: [[-2, 2]]
    
    # Example 2:
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k2 = 2
    print("Example 2 Output:", k_closest_points_to_origin(points2, k2))
    # Expected output: Two closest points, e.g., [[3, 3], [-2, 4]]
    
# Time and Space Complexity Analysis:
#
# Time Complexity: O(n log k)
#   - We process each of the n points, and each heap operation takes O(log k).
#
# Space Complexity: O(k)
#   - We maintain a heap of size k.
