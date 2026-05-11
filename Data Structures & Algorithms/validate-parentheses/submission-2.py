class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for c in s:
            if c == '(' or c == '['  or c == '{':
                stack.append(c)
            elif c == ')' or c == ']'  or c == '}':
                # take a look at the last stack
                if len(stack) > 0:
                    last_c = stack.pop()

                    if (c == ')' and last_c != '('):
                        return False
                    elif (c == ']' and last_c != '['):
                        return False
                    elif (c == '}' and last_c != '{'):
                        return False
                else:
                    return False
                
        if len(stack) > 0:
            return False
        else:
            return True