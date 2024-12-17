#Given two strings s and t, return true if t is an anagram
#of s, and false otherwise.


def valid_anagram(s, t):
    #use two frequency dictionary and compare the two to determine anagram

    s_dict = {}
    t_dict = {}

    for char in s:
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1

    for char in t:
        if char in t_dict:
            t_dict[char] += 1
        else:
            t_dict[char] = 1
    
    return s_dict == t_dict

#comment - dictonary works for anagram but not palindrome since order & specific amount matters!