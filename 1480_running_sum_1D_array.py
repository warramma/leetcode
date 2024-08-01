#tags: prefix
#date: 8-1-24
#difficulty: easy
#time complexity: O(n)
#space complexity: O(1)

#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

#Example 1:

#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(self, nums: List[int]) -> List[int]:
    #create an array to hold running sums
    #create sum variable
    #using for loop, iterate over nums and append sum
    #return running sum array
    running_sums = []
    sum = 0
    for i in range(len(nums)):
        sum  = sum + nums[i]
        running_sums.append(sum)
    return running_sums