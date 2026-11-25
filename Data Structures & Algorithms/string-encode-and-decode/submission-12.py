class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for i in strs:
            word += str(len(i)) + "#" + i
        return word
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Step 1: move j forward from i until s[j] is "#"
            j = i
            while s[j] != "#":
                j += 1

            # the length is the characters from i up to j (not including the #)
            length = int(s[i:j])

            # Step 2: the word starts right after the #, and ends at start + length
            start = j+1
            word = s[start : start + length]
            result.append(word)

            # Step 3: move i to where the next length begins
            i = start + length

        return result