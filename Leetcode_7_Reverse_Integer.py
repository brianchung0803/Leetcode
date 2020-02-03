class Solution:
    def reverse(self, x: int) -> int:
        if(x==0):
            return 0
        
        output=str(abs(x))[::-1]
        if(x<0):
            ans=int(output)*-1
            if(ans<-pow(2,31)):
                return 0
            else:
                return ans
        
        else:
            if(int(output)>pow(2,31)-1):
                return 0
            else:
                return int(output)
