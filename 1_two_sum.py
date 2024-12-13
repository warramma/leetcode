'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''


#time complexity - O(n^2) - notice use of .index() within a for loop is O(n^2)
#space complexity - O(n) - set takes O(n) storage

def twoSum(self, nums: List[int], target: int) -> List[int]:
       #each input has a unique solution, same element can be used twice. any order is fine. 

       #match/plan - dynamic programming solution, keep track of valid possibilities using a st
       #initialize a set then iterate through the given array
       #check if the target- nums[current index] is in the set, if yes, then
       #save the difference and the current num and find the indices using .index()
       #if not, add the current num to the set and continue

       checked = set()
       differenceIndex = None
       currentIndex = None
       for i in range(len(nums)):
            if target - nums[i] in checked:
                differenceIndex = nums.index(target-nums[i])
                currentIndex = i
                return [differenceIndex, currentIndex]
            else:
                checked.add(nums[i])


#IMPROVED SOLUTION
def twoSumImproved(target, nums):
     #dynamic programming approach
     #use a dictionary to keep track of seen, key is the difference, and the value is the index
     #iterate through list of nums, find the difference if in seen, then return a list of the two indices
     #otherwise add diff to seen with value of i

     seen = {}
     for i in range(len(nums)):
          diff = target - nums[i]
          if diff in seen:
               return [seen[diff], i]
          else:
               seen[nums[i]] = i