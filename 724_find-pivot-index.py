#724 - find pivot index
#tags: prefix, postfix
#date: 8-6-24
#difficulty: easy/medium
#time complexity: O(n)
#space complexity: O(1)
#------------------------------------------------------------

#explanation: create two variables leftsum and rightsum to keep 
#track of prefix sum and postfix sum. 
#notice that rightsum is really the total sum minus the leftsum 
#minus the pivot
#update leftsum (prefix) with next element in nums
#check until sums are equal, else return -1

#----------------------------------------------------------
#DESCRIPTION
#----------------------------------------------------------
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = 0
        total = sum(nums)
        for i in range(len(nums)):
            rightsum = total - leftsum - nums[i]
            if(leftsum == rightsum):
                return i
            leftsum += nums[i]
        return -1