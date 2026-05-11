class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert strs into their binary representation, the key of the hash map is 26 integer vector
        hash_table = {}
        for curr_str in strs:
            int_vec = [0] * 26
            for c in curr_str:
                c_int = ord(c) - 97
                int_vec[c_int] += 1
            
            hash_key = tuple(int_vec)
            if hash_key in hash_table:
                hash_table[hash_key].append(curr_str)
            else:
                hash_table[hash_key] = [curr_str]
    
        res = []
        for key, str_val in hash_table.items():
            res.append(str_val)
        
        return res
