class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp=[[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        
        column=True
        row=True
       
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if(obstacleGrid[i][j]==1):
                    if(i==0 and j==0):
                        column=False
                        row=False
                    elif(i==0):
                        column=False   
                    elif(j==0):
                        row=False
                    dp[i][j]=0
                    
                elif (i==0 or j==0):
                    if(i==0 and column==False):
                        dp[i][j]=0
                    elif(j==0 and row==False):
                        dp[i][j]=0
                    else:
                        dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return dp[-1][-1]
