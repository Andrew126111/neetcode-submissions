class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for words in strs:
            arr = [0]*26
            for char in words:
                idx = ord("a") - ord(char)
                arr[idx]+=1
            tup = tuple(arr)
            map[tup].append(words)
        return list(map.values())
        

            

        



