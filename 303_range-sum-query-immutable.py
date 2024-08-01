#303 - Range Sum Query Immutable
#tags: prefix
#date: 8-1-24
#difficulty: easy
#time complexity: O(n)
#space complexity: O(1)
#-----------------------------------------------------------
#Given an integer array nums, handle multiple queries of the following type:
#Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
#Implement the NumArray class:

#NumArray(int[] nums) Initializes the object with the integer array nums.
#int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

#Example 1:
#Input
#["NumArray", "sumRange", "sumRange", "sumRange"]
#[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
#Output
#[null, 1, -1, -3]

#-------------------------------------------------------------
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0]
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            self.prefixSum.append(sum)
        
    def sumRange(self, left: int, right: int) -> int:
        answer = self.prefixSum[right + 1] - self.prefixSum[left]
        return answer       


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)