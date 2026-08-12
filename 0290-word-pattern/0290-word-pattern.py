class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        connect={}
        s=s.split(' ')
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in connect and s[i]!=connect[pattern[i]]:
                return False
            elif pattern[i] not in connect and s[i] in connect.values():
                return False
            else:
                connect[pattern[i]]=s[i]
        return True