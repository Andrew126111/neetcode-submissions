class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] #create a stack just array
        hashClose = {")":"(", "}":"{", "]":"[" } # create hashmap with closing as keys
        for char in s: #loop through the original string
            if char in hashClose: # we want to check if closing is in hashmap
                if stack and stack[-1] == hashClose[char]: #if yes then we want to know if the top element is equal to the opening paranthesis
                    stack.pop() # if yes we want to pop it from the top
                else:
                    return False
            else:
                stack.append(char) # ifthe character is not in the hashclose we want to add it to our stack
        return True if not stack else False#after looping we need to return true if the stack is empty because we are popping everything if not then we return flase