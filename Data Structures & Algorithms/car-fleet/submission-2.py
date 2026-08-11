class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(speed)):
            arr.append((position[i], speed[i]))
        arr.sort(key = lambda x: x[0], reverse=True)
        stack = []
        for car in arr:
            time = (target-car[0])/car[1]
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)