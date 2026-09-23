class Solution(object):
    def isValid(self, s):
        stack = []

        maps = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in maps:
                stack.append(maps[char])
            else:
                if not stack or stack[-1] != char:
                    return False

                stack.pop()
        

        return len(stack) == 0