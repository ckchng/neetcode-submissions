class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            len_str = len(string)
            encoded = encoded + str(len_str) + '#' + string
        return encoded
    
    def decode(self, s: str) -> List[str]:
        # read until '#', retrieve the number of characters
        num_str = ''
        decoded = []
        i = 0 
        while i < len(s):
            char = s[i]
            if char != '#':
                num_str = num_str + char
                i += 1
            else:
                # hit '#'
                num_str = int(num_str)
                decoded.append(s[i+1:i+1+num_str])
                i += num_str + 1
                num_str = ''

        return decoded