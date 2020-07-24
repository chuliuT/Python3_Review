class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dict = {"(": ')', '[': ']', '{': '}'}
        for data in s:
            if data in dict.keys():
                stack.append(data)
            elif stack:
                top = stack.pop()
                if dict[top] != data:
                    return False
            else:
                return False
        return False if stack else True