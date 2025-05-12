"""
🔷 LeetCode 295 - Find Median from Data Stream

📘 Problem:
Design a data structure that efficiently supports the following operations:
1. Add a number from a stream of integers.
2. Find the median of all added numbers.

The median is:
- The middle value in an odd-length list.
- The average of the two middle values in an even-length list.

🧠 Example:
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output:
[null, null, null, 1.5, null, 2.0]

🔒 Constraints:
- -10⁵ <= num <= 10⁵
- At most 5 * 10⁴ calls to `addNum` and `findMedian`
- There will be at least one element before calling `findMedian`

📍 Follow-up:
- If 99% of values are in [0,100], can you optimize?
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Max heap for lower half (invert sign)
        self.min_heap = []  # Min heap for upper half

    def addNum(self, num: int) -> None:
        # Step 1: Add to max-heap
        heapq.heappush(self.max_heap, -num)

        # Step 2: Move max of max-heap to min-heap to keep order
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Step 3: Balance sizes (max_heap can have at most 1 more element)
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return self.min_heap[0]        	
        return (-self.max_heap[0] + self.min_heap[0]) / 2



class OptimizedMedianFinder:
    def __init__(self):
        self.buckets = [0] * 101  # For values in [0, 100]
        self.count = 0
        self.lower = []  # max heap for < 0
        self.higher = []  # min heap for > 100

    def addNum(self, num: int) -> None:
        self.count += 1
        if 0 <= num <= 100:
            self.buckets[num] += 1
        elif num < 0:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.higher, num)

    def findMedian(self) -> float:
        mid1 = self.count // 2
        mid2 = mid1 if self.count % 2 else mid1 - 1
        i, acc = -1, 0

        def get_kth(k):
            nonlocal i, acc
            # Check lower heap
            if k < len(self.lower):
                return -heapq.nsmallest(len(self.lower), self.lower)[k]

            k -= len(self.lower)
            for val in range(101):
                acc += self.buckets[val]
                if acc > k:
                    return val
            return heapq.nsmallest(len(self.higher), self.higher)[k - acc]

        if self.count % 2:
            return get_kth(mid1)
        else:
            return (get_kth(mid1) + get_kth(mid2)) / 2




# 🔸 Example usage
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # Output: 1.5
    mf.addNum(3)
    print(mf.findMedian())  # Output: 2.0

"""
🧠 Time and Space Complexity:

addNum(num):
⏱ Time: O(log n) — due to heappush/heappop operations
💾 Space: O(n) — to store all elements across two heaps

findMedian():
⏱ Time: O(1) — just reading tops of heaps
💾 Space: O(1)

Follow-up optimizations:
- If most values are in [0,100], use a bucket counting method and only use a heap for rare outliers.


# 🔁 1. Heap-Based Approach (General Purpose)
# ✅ Pros:
# Works for any range of integers.

# Handles dynamic and unpredictable value distributions well.

# Accurate and stable for real-time insertions and queries.

# ⏱️ Time Complexity:
# addNum(): O(log n) — due to heappush and heappop.

# findMedian(): O(1) — just reads top(s) of heaps.

# 💾 Space Complexity:
# O(n) — stores all elements across two heaps.

# 💡 Best For:
# General scenarios with wide or unknown value ranges (e.g., [-10⁵, 10⁵]).

# 🧊 2. Bucket-Based Approach (Optimized for values in [0,100])
# ✅ Pros:
# Very fast and memory-efficient for fixed, small value ranges.

# Ideal if 99% of input is in [0,100].

# Fast addNum (O(1)) and fast findMedian when values are mostly in-bucket.

# ⏱️ Time Complexity:
# addNum():

# O(1) for [0,100]

# O(log k) if num is an outlier (using heaps for <0 or >100)

# findMedian():

# O(1–101) — scanning a small fixed-size array.

# 💾 Space Complexity:
# O(1) for in-range (101 buckets).

# O(k) for outliers (heap size k).

# ⚠️ Cons:
# Requires prior knowledge of value distribution.

# Falls back to heap logic if too many outliers exist.

# Needs logic for computing kth element when buckets + heaps are combined.

# 💡 Best For:
# Streams where values are mostly in a fixed narrow range like sensor data, ratings, percentages.


