class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cursor = 0;
        for i in range(len(s)):
            found = False;
            for j in range(cursor, len(t)):
                if s[i] == t[j]:
                    found = True;
                    cursor = j + 1;
                    break;
            if not found:
                return False;
        return True;
                
                

