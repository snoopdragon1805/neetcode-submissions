class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for ch in path:
            if ch == "..":
                if stack:
                    stack.pop()
            elif ch =="." or ch =="":
                continue
            else:
                stack.append(ch)
        return "/"+"/".join(stack)