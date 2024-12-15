'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

#solution 1


def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char)
        

        cleaned_string = ''.join(cleaned)

        reversed_string = cleaned_string[::-1]

        return cleaned_string.lower() == reversed_string.lower()


#using list comprehension

def isPalindrome(self, s: str) -> bool:
        cleaned = [char.lower() for char in s if char.isalnum()]

        left, right = 0, len(cleaned) -1

        while left < right:
            if cleaned[right] != cleaned[left]:
                return False
            left += 1
            right -= 1

        return True