class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ind, item in enumerate(asteroids):
            if item<0:
                smash = 1
                while len(stack)>0 and smash:
                    prev = stack[-1]
                    if prev<0:
                        stack.append(item)
                        smash=0
                    elif abs(item)>prev:
                        stack.pop()
                    elif abs(item) == prev:
                        stack.pop()
                        smash=0
                    else:
                        smash=0
                if smash==1:
                    stack.append(item)
            else:
                stack.append(item)
        return stack
