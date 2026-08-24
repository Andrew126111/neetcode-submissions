class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0] * len(temperatures)
        stack=[] # we want two values

        for i,t in enumerate(temperatures): # we have teh index and value
            while stack and t> stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd # we do this to get how many days in between
            stack.append([t,i])
        return result