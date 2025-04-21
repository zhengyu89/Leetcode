class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = "";
        counter = 0;
        minlen = min(len(word1),len(word2));
        for i in range (minlen):
                result += word1[i];
                result += word2[i];
                counter+= 1;
                
        if (len(word1) > len(word2)):
            for j in range (counter,len(word1)):
                result += word1[j];
        if (len(word1) < len(word2)):
            for j in range (counter,len(word2)):
                result += word2[j];
        return result;

def main():
    sol = Solution();
    word1 = "abcd";
    word2 = "pq";
    print(sol.mergeAlternately(word1, word2));
