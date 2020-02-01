class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if(numRows==0):
            return []
        if(numRows==1):
            return [[1]]
        next=self.generate(numRows-1)
        return self.construct(next,numRows)
    
    def construct(self,next,num):
        if(num==2):
            tmp=[1,1]
            next.append(tmp)
            return next
        
        answer=[0 for i in range(num)]
        for i in range(1,len(answer)-1):
            answer[i]=next[num-2][i]+next[num-2][i-1]
        answer[0]=1
        answer[-1]=1
        next.append(answer)
        return next
