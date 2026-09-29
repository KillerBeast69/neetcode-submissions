from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['{','(','[']
        closed = ['}',')',']']

        stack = deque()

        for i in s:
            if i in opened:
                stack.append(i)
            if i in closed:
                if len(stack) == 0:
                    return False
                return stack.pop() == opened[closed.index(i)]

        return len(stack) == 0
        