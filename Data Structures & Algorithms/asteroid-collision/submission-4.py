class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in asteroids:
            # A collision only happens if the top of stack is moving RIGHT ( > 0)
            # and the current asteroid is moving LEFT ( < 0)
            while stack and i < 0 < stack[-1]:
                if stack[-1] < abs(i):
                    stack.pop()  # Top asteroid is destroyed; keep checking
                    continue
                elif stack[-1] == abs(i):
                    stack.pop()  # Both asteroids destroy each other
                break  # Current asteroid 'i' is destroyed or tied; stop checking
            else:
                # This executes ONLY if the while loop didn't hit a 'break'
                # (meaning 'i' survived all collisions or didn't collide at all)
                stack.append(i)
                
        return stack
