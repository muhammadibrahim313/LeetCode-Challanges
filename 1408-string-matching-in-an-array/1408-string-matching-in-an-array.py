class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n=len(words)
        ans=[]
        for i in range(n):
            for j in range(i+1,n):
                if words[i] in words[j] and words[i] not in ans:
                    ans.append(words[i])
                elif words[j] in words[i] and words[j] not in ans:
                    ans.append(words[j])
        return ans