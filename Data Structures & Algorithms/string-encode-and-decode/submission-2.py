class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = s.index("#", i)          # fine del numero
            print(j )
            length = int(s[i:j])
            print( int(s[i:j]))
            start = j + 1
            out.append(s[start:start + length])
            i = start + length           # salta esattamente length caratteri
        return out
