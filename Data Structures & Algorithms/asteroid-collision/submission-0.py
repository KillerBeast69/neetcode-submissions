class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
            elif (a * stack[-1] > 0):
                stack.append(a)
            else:
                top = stack[-1]
                while (a * top < 0):
                    if abs(a) > abs(top):
                        stack.pop()
                    elif abs(a) < abs(top):
                        break
                    else:
                        #both are equal
                        stack.pop()
                        break
        return stack
                