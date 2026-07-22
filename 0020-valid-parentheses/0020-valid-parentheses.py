class Solution:
    def isValid(self, s: str) -> bool:
        is_valid=True
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack)!=0:
                    if ((i==')' and stack[-1]=='(') or (i==']' and stack[-1]=='[') or (i=='}' and stack[-1]=='{')):
                        stack.pop()
                    else:
                        is_valid=False
                else:
                    is_valid=False
                    break
        if len(stack)!=0:
           is_valid=False
        return is_valid
