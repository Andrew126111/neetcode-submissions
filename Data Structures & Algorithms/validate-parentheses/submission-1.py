class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap = {")" : "(", "}":"{", "]":"["}
        for c in s:
            if c in hashmap: #checks if its a closing
                if stack and stack[-1]==hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False