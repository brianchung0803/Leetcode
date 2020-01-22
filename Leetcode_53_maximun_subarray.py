class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        if len(nums)==1:
            return nums[0]
        
        ans=nums[0]
        num=nums[0]
        for i in nums[1:]:
            num=max(i,num+i)
            ans=max(num,ans)

        return ans
