class Solution:
    def isValid(self, s: str) -> bool:
        # the first time you see a close one, it has to match the latest open.
        # o(n) o(n)
        # store every open one in a stack.
        # once you hit a close one
        # pop the open stack, if it matches, great, else, return False
        open_stack = []
        if len(s) == 1:
            return False
        for p in s:
            if p == '(' or p == '[' or p == '{':
                open_stack.append(p)
            else:
                if len(open_stack) == 0:
                    return False
                curr_open = open_stack.pop() # LIFO
                if curr_open == '(' and p != ')' or \
                curr_open == '[' and p != ']' or \
                curr_open == '{' and p != '}':
                    return False
        if len(open_stack) > 0:
            return False
        else:
            return True