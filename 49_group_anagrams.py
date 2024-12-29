# 49. Group Anagrams
# Solved
# Medium
# Topics
# Companies
# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

def groupAnagrams(strs):
    result = {}
    for string in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1
        
        key = tuple(count)

        if key in result:
            result[key].append(string)
        else:
            result[key] = [string]
    return list(result.values())