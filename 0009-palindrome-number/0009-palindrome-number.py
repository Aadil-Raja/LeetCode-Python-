class Solution(object):
    def isPalindrome(self, x):
        temp=x
        newnum=0
        if x<0:
            return False
        while temp != 0:
            digit=temp%10
            newnum=newnum*10+digit
            temp/=10
        if newnum==x:
            return True
        return False
        