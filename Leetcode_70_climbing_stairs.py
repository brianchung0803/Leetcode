class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n==0:
            return 0
        if n==1:
            return 1

        ways=[]
        for i in range(n+1):
            ways.append(0)
    
        ways[0]=0
        ways[1]=1                             
        ways[2]=2
        for i in range(3,n+1):
            ways[i]=ways[i-1]+ways[i-2]
        
        return ways[n]
