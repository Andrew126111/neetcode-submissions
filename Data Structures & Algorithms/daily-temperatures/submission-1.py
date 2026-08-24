class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0] * len(temperatures)
        stack=[] # [temp, index]

        for indx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackTemp, stackIndx = stack.pop() # this pops both values
                res[stackIndx] = (indx - stackIndx)
            stack.append((val, indx))
        return res

