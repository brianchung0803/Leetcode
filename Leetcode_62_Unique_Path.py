class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.factorial(m+n-2)/(self.factorial(m-1)*self.factorial(n-1))
        
        
    def factorial(self,num):
        if (num==1 or num==0):
            return 1
        else: 
            tmp=self.factorial(num-1)
            return tmp*num
