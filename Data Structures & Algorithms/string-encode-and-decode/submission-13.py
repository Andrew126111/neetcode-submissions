class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for i in strs:
            word += str(len(i)) + "#" + i
        return word
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            start = j+1
            word = s[start : start + length]
            res.append(word)
            i = start + length
        return res

    