class Solution(object):
    def isPalindrome(self, n):
        if n< 0:
            return False
        temp=n
        rev=0
        while(n>0):
            dig=n%10
            rev=rev*10+dig
            n=n//10
        if(temp==rev):
            return True
        else:
            return False