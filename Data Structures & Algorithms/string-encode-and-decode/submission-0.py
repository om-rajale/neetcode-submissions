class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        # Store: length + '#' + word
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        # Final decoded list
        res = []
        # Starting index
        i = 0
        while i < len(s):
            # Find '#'
            j = i
            while s[j] != "#":
                j += 1
            # Read length before '#'
            length = int(s[i:j])
            # Read the next 'length' characters
            word = s[j + 1 : j + 1 + length]
            # Save the word
            res.append(word)
            # Move to the next encoded string
            i = j + 1 + length
        return res