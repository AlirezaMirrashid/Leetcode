"""
🔷 LeetCode 27 – Remove Element

🧠 Problem Summary:
Given an array `nums` and a value `val`, remove all instances of `val` in-place and return the new length `k`.
The first `k` elements of `nums` should contain the elements not equal to `val`.

✅ Constraints:
- Do it in-place with O(1) extra memory.
- The relative order of elements can be changed.
- Return only the number of remaining valid elements.

---

📌 Example 1:
Input: nums = [3,2,2,3], val = 3  
Output: 2, nums = [2,2,_,_]

📌 Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2  
Output: 5, nums = [0,1,4,0,3,_,_,_]

---

💡 Core Idea:
Use a pointer to overwrite elements not equal to `val`.
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# -------------------------
# 🔸 Example test cases
if __name__ == "__main__":
    sol = Solution()

    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = sol.removeElement(nums1, val1)
    print(f"Output: {k1}, nums = {nums1[:k1]}")

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = sol.removeElement(nums2, val2)
    print(f"Output: {k2}, nums = {nums2[:k2]}")

"""
⏱ Time Complexity: O(n)
    - Iterate once through the list

💾 Space Complexity: O(1)
    - Constant extra space
"""
