class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i == "]":
                rev=""
                while stack[-1]!="[":
                    rev = stack.pop()+rev
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                num = int(num)
                stack.append(num*(rev))
            else:
                stack.append(i)
        return "".join(stack)