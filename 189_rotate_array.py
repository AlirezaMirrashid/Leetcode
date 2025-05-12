"""
🔷 LeetCode 189 – Rotate Array

🧠 Problem Summary:
Given an array `nums`, rotate it to the right by `k` steps (0 ≤ k ≤ 10^5).
Each element is shifted to the right `k` times, and the elements at the end wrap around to the front.

✅ Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

---

📌 Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3  
Output: [5,6,7,1,2,3,4]

📌 Example 2:
Input: nums = [-1,-100,3,99], k = 2  
Output: [3,99,-1,-100]

---

💡 Core Idea:
There are multiple approaches:
1. **Extra Array** – Copy to a new list with correct rotated index.
2. **Reverse Trick** – Reverse the entire array, then reverse parts.
3. **Cyclic Replacement** – Track and shift elements one by one (O(1) space).
"""

from typing import List

class Solution:
    def rotate_reverse(self, nums: List[int], k: int) -> None:
        """
        ✅ In-place rotation using reverse.
        """
        n = len(nums)
        k %= n

        def reverse(l: int, r: int):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

    def rotate_extra_space(self, nums: List[int], k: int) -> None:
        """
        ✅ O(n) time and space solution using an extra array.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

    def rotate_cyclic(self, nums: List[int], k: int) -> None:
        """
        ✅ Cyclic replacements. O(n) time, O(1) space.
        """
        n = len(nums)
        k %= n
        count = 0
        start = 0

        while count < n:
            current = start
            prev = nums[start]
            while True:
                nxt = (current + k) % n
                nums[nxt], prev = prev, nums[nxt]
                current = nxt
                count += 1
                if start == current:
                    break
            start += 1


# 🔸 Example test cases
if __name__ == "__main__":
    sol = Solution()

    arr1 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate_reverse(arr1, 3)
    print("Reverse method:", arr1)  # [5, 6, 7, 1, 2, 3, 4]

    arr2 = [-1, -100, 3, 99]
    sol.rotate_extra_space(arr2, 2)
    print("Extra space method:", arr2)  # [3, 99, -1, -100]

    arr3 = [1, 2, 3, 4, 5, 6]
    sol.rotate_cyclic(arr3, 2)
    print("Cyclic method:", arr3)  # [5, 6, 1, 2, 3, 4]

"""
⏱ Time Complexity:
- Reverse method: O(n)
- Extra space: O(n)
- Cyclic replacement: O(n)

💾 Space Complexity:
- Reverse method: O(1)
- Extra space: O(n)
- Cyclic replacement: O(1)
"""
