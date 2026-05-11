class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for str in strs:
            cum_bin_rep = [0] * 26
            for c in str:
                i = ord(c) - 97
                cum_bin_rep[i] += 1
            
            key = tuple(cum_bin_rep)
            if key not in hash:
                hash[key] = []
            hash[key].append(str)
        
        output = []
        for key in hash:
            output.append(hash[key])
        
        return output
    