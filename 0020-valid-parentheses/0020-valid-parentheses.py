class Solution(object):
    def isValid(self, s):
        x = []
        size = -1
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                x.append(s[i])
                size += 1
            elif s[i] == ")":
                if size == -1 or x[size] != "(":
                    return False
                x.pop()
                size -= 1
            elif s[i] == "]":
                if size == -1 or x[size] != "[":
                    return False
                x.pop()
                size -= 1
            elif s[i] == "}":
                if size == -1 or x[size] != "{":
                    return False
                x.pop()
                size -= 1
        
        return size == -1