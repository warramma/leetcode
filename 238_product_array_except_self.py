#238 - product of array except self
#tags: prefix, postfix
#date: 8-1-24
#difficulty: medium
#time complexity: O(n)
#space complexity: O(1)
#-----------------------------------------------------------
#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation. 

#Example 1:

#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]
#------------------------------------------------------------
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create two arrays, one postfix and one prefix multiplication
        #use two separate for loops to create both arrays
        #to get desired answer, use product up to index on either side and multiply
        #aka prefix answer * postfix answer, then append to exceptSelf

        prefix = [1]
        product = 1
        for i in range(len(nums)):
            product = product * nums[i]
            prefix.append(product)
        print('prefix: ', prefix)

        postfix = [None] * len(nums)
        postfixproduct = 1
        for i in range(len(nums)-1, -1, -1):
            postfixproduct = postfixproduct * nums[i]
            postfix[i] = postfixproduct
        postfix.append(1) #to account for postfix[i + 1] for last index in exceptSelf
        print('postfix: ', postfix)
        
        exceptSelf = []
        for i in range(len(nums)):
            exceptSelf.append(prefix[i] * postfix[i+1])
        
        return exceptSelf
