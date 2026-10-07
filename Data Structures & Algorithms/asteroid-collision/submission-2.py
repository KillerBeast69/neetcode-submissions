class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for i in asteroids:

            while stack and stack[-1] > 0 and i < 0:

                if stack[-1] < abs(i):
                    stack.pop()

                elif stack[-1] == abs(i):
                    stack.pop()
                    i = 0
                    break

                else:
                    i = 0
                    break

            if i != 0:
                stack.append(i)

        return stack