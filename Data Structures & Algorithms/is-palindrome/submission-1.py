class Solution:
    def isPalindrome(self, s: str) -> bool:
        # definition of a palindrome,
        # the i and n - i is the same
        out = []
        for c in s:
            if c.isalnum():
                out.append(c.lower())
        out = "".join(out)
        for i in range(len(out)):
            if out[i] != out[len(out)- 1 - i]:
                return False
        return True
