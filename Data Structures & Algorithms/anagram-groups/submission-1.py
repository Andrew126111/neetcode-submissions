class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                sig = ord(j)- ord("a")
                count[sig]+=1
            tup = tuple(count)
            dict[tup].append(i)
        return list(dict.values())


        
            

        



