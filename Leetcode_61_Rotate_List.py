# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if(head==None):
            return head
        
        ans=[]
        
        tmp=head
        
        while(tmp!=None):
            ans.append(tmp.val)
            tmp=tmp.next
       
        k=k%len(ans)
        j=len(ans)-1
        for i in range(k):
            int_tmp=ans[-1]
            while(j>0):
                ans[j]=ans[j-1]
                j-=1
            ans[0]=int_tmp
            j=len(ans)-1
        
        node_ans=head
        head.val=ans[0]
        for i in ans[1:]:
            head=head.next
            head.val=i
            
        return node_ans
        
