class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        arr=[]
        for i in range(n):
            arr.append([position[i], speed[i]])
        arr.sort(key = lambda x:x[0], reverse = True)
        stack=[]
        for i in arr:
            time = (target-i[0])/i[1]
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)
