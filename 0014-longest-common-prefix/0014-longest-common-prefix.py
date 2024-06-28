class Solution(object):
    def longestCommonPrefix(self, strs):
      
            x= ""
            n=len(strs[0])
            for i in range(n):
                for s in strs:
                    if  i == len(s) or strs[0][i] != s[i]:
                        return x
                x=x+strs[0][i]
        
            return x