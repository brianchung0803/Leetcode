class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l=len(s)
        if(l<=1):
            return
        
        for i in range(l/2):
            tmp=s[i]
            s[i]=s[l-i-1]
            s[l-i-1]=tmp
        return
