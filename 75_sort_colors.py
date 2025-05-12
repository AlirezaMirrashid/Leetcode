"""
🔷 LeetCode 75 – Sort Colors

🧠 Problem Summary:
Given an array `nums` with n objects colored red (0), white (1), or blue (2), sort them in-place so that objects of the same color are adjacent, with the order red → white → blue.

✅ Constraints:
- Must sort in-place
- No library sort function
- 1 ≤ n ≤ 300

---

📌 Example:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

---

💡 Solution 1 (Two Pass Counting Sort):
- Count number of 0s, 1s, and 2s, then overwrite the array.

💡 Solution 2 (Dutch National Flag, One Pass):
- Use three pointers → `low`, `mid`, `high`
- Swap 0s to front, 2s to end, leave 1s in the middle
"""

class Solution:
    def sortColorsCountingSort(self, nums):
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):
            for _ in range(count[i]):
                nums[index] = i
                index += 1

    def sortColorsDutchFlag(self, nums):
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    arr1 = [2,0,2,1,1,0]
    arr2 = [2,0,1]
    sol.sortColorsCountingSort(arr1)
    print(arr1)  # [0,0,1,1,2,2]
    sol.sortColorsDutchFlag(arr2)
    print(arr2)  # [0,1,2]

"""
⏱ Time Complexity:
- Both solutions: O(n)

💾 Space Complexity:
- Counting sort: O(1)
- Dutch flag: O(1) (constant space, in-place)
"""
