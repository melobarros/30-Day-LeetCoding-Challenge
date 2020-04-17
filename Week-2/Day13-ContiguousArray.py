"""
Day 13 - Contiguous Array
Leetcode Medium Problem

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
  Input: [0,1]
  Output: 2
  Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
  Input: [0,1,0]
  Output: 2
  Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
  
Note: The length of the given binary array will not exceed 50,000.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxL = 0
        partialSum = 0
        idxDic = {0: -1}
        
        for idx, num in enumerate(nums):
            if num: partialSum += 1
            else: partialSum -= 1
            
            if partialSum in idxDic:
                maxL = max(maxL, (idx - idxDic[partialSum]))
            else:
                idxDic[partialSum] = idx
                
        return maxL
