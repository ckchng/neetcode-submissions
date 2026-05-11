class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first merge them, remove the space and comma and ':'
        clean = "".join(c for c in s if c.isalnum())

        # then do two-pointer check, remember to be case insensitive too
        left = 0
        right = len(clean) - 1
        while left < right:
            if clean[left].lower() == clean[right].lower():
                left += 1
                right -= 1
            else:
                return False    
        
        return True
    