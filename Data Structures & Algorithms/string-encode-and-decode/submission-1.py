class Solution:
    def encode(self, strs: List[str]) -> str:
        # turn it into ord
        out = ""
        for s in strs:
            for c in s:
                out += str(ord(c)) 
                out += "#"
            out += '+'
        

        return out

    def decode(self, s: str) -> List[str]:
        curr_word = ""
        curr_char = ""
        res = []
        for c in s:
            if c == '#':
                curr_word += chr(int(curr_char))
                curr_char = ""
            elif c == '+':
                res.append(curr_word)
                curr_word = ""
            else:
                curr_char += c
        
        return res