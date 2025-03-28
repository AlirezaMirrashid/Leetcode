# LeetCode 1570: Dot Product of Two Sparse Vectors
# Problem Link: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

# Example 1:

# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

# Example 2:

# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
# Example 3:

# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6
 

# Constraints:

# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 100

# hashmap is not a good answer according to https://www.youtube.com/watch?v=sQNN4xKC1mA

from typing import List, Optional

class SparseVector:
    """
    A class representing a sparse vector, storing only non-zero elements as (index, value) pairs.
    
    The dot product computation is optimized using a two-pointer technique, which allows for efficient 
    calculation in O(k + m) time complexity, where k and m are the number of non-zero elements 
    in the respective vectors.
    """

    def __init__(self, nums: List[int]) -> None:
        """
        Initializes the SparseVector with a given list of numbers.
        
        Stores only the non-zero elements along with their indices to optimize space usage.
        
        Parameters:
            nums (List[int]): The input vector represented as a list.
        """
        self.elements: List[List[int]] = [[i, num] for i, num in enumerate(nums) if num != 0]
        self.length: int = len(nums)

    def dot_product(self, other: 'SparseVector') -> Optional[int]:
        """
        Computes the dot product of this vector with another SparseVector.
        
        The function uses a two-pointer approach to efficiently compute the dot product by iterating 
        only over non-zero elements of both vectors.
        
        Parameters:
            other (SparseVector): The other sparse vector to compute the dot product with.
        
        Returns:
            Optional[int]: The dot product result if the vectors have the same length, else None.
        """
        if self.length != other.length:
            return None
        
        i, j = 0, 0
        dot_product_result = 0

        while i < len(self.elements) and j < len(other.elements):
            index1, value1 = self.elements[i]
            index2, value2 = other.elements[j]

            if index1 < index2:
                i += 1
            elif index1 > index2:
                j += 1
            else:
                dot_product_result += value1 * value2
                i += 1
                j += 1
        
        return dot_product_result


# Example Usage:
if __name__ == "__main__":
    vec1 = SparseVector([0, 1, 0, 0, 2, 0, 0])
    vec2 = SparseVector([1, 0, 0, 0, 3, 0, 4])

    result = vec1.dot_product(vec2)
    print(f"Dot Product Result: {result}")  # Expected output: 6

# Time and Space Complexity Analysis:
#
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
