class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if(len(buildings)==0):
            return []
        if(len(buildings)==1):
            return[[buildings[0][0],buildings[0][2]],[buildings[0][1],0]]
        
        middle=(len(buildings)-1)/2
        
        left=self.getSkyline(buildings[0:middle+1])
        right=self.getSkyline(buildings[middle+1:])
        
        return self.conquer(left,right)
        
    def conquer(self,left,right):
        l=0
        r=0
        return_list=[]
        hl=-1
        hr=-1
        while(l<len(left) and r<len(right)):
            if(left[l][0]<right[r][0]):
                hl=left[l][-1]
                tmp=[left[l][0],max(hl,hr)]
                if(return_list==[] or return_list[-1][1]!=tmp[1]):
                    return_list.append(tmp)
                l+=1
            elif(left[l][0]>right[r][0]):
                hr=right[r][-1]
                tmp=[right[r][0],max(hl,hr)]
                if(return_list==[] or return_list[-1][1]!=tmp[1]):
                    return_list.append(tmp)
                r+=1
            else:
                hl=left[l][-1]
                hr=right[r][-1]
                tmp=(left[l][0],max(hl,hr))
                if(return_list==[] or return_list[-1][1]!=tmp[1]):
                    return_list.append(tmp)
                l+=1
                r+=1
        while l<len(left):
            if(return_list==[] or return_list[-1][1]!=left[l][-1]):
                return_list.append(left[l])
            l+=1
        while r<len(right):
            if(return_list==[] or return_list[-1][1]!=right[r][-1]):
                return_list.append(right[r])
            r+=1
            
        return return_list
        