class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for i in strs:
            length = str(len(i)) + "#"
            code += length + i
        
        return code

    def decode(self, s: str) -> List[str]:
        dis = []
        length  = ""

        x = 0
        while x < len(s):
            
            if s[x] != "#":
                length += s[x]
            
            else:
                dis.append(s[x + 1:(int(length)+x+1)])
                x += int(length)
                length = ""
            
            x += 1
        
        return dis