class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        node=0
        judge={}
        length=len(wall)
        for line in range(length):
            tmp=0
            node+=len(wall[line])
            for vertex in wall[line]:
                tmp+=vertex
                judge.setdefault(tmp,0)
                judge[tmp]+=1

        judge.setdefault(0,0)
        
        max_key=0
        max_value=0
        
        for key,value in judge.items():
            if(key!=tmp and value>max_value):
                max_value=value
                max_key=key
                
        ans=length-judge[max_key]
        
        return ans
