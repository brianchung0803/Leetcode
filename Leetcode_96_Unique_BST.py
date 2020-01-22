class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        
        num=[]
        for i in range(n+1):
            num.append(0)
        
        num[0]=1
        for j in range(1,n+1):
            left=j-1
            right=0
            while(left>=0):
                num[j]+=num[left]*num[right]
                left-=1
                right+=1
    
        return num[n]
