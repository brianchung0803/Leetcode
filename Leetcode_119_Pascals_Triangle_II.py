class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if(rowIndex==0):
            return [1]
        
        next=self.getRow(rowIndex-1)
        
        return self.construct(next,rowIndex)
    
    
    def construct(self,next,row):
        if(row==1):
            return [1,1]
        else:
            return_answer=[0 for i in range(row+1)]
            for i in range(1,len(next)):
                return_answer[i]=next[i-1]+next[i]
            return_answer[0]=1
            return_answer[-1]=1
        
        
        return return_answer
