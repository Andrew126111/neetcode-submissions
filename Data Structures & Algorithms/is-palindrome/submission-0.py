class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        end = len(newStr)-1
        for i in range(0,len(newStr)//2):
            if newStr[i]!=newStr[end]:
                return False
            end -=1
        return True
            

