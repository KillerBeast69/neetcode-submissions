class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
            elif (a * stack[-1] > 0):
                stack.append(a)
            else:
                while (a * stack[-1] < 0):
                    if abs(a) > abs(stack[-1]):
                        stack.pop()
                    elif abs(a) < abs(stack[-1]):
                        break
                    else:
                        #both are equal
                        stack.pop()
                        break
        return stack
                