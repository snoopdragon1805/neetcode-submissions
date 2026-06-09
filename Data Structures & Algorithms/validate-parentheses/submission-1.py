class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="(" :
                stack.append(')')
            elif i == "[" :
                stack.append("]")
            elif i=="{":
                stack.append("}")
            elif i == ")" or i == "}" or i == "]":
                if len(stack)>0 and stack[-1] == i:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False