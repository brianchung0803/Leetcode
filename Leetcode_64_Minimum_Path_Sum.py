 for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i==0 and j==0):
                    continue
                elif(i==0):
                    grid[i][j]+=grid[i][j-1]
                    continue
                elif(j==0):
                    grid[i][j]+=grid[i-1][j]
                    continue
                tmp_up=grid[i][j]+grid[i-1][j]
                tmp_left=grid[i][j]+grid[i][j-1]
                grid[i][j]=min(tmp_up,tmp_left)
        
        ans=grid[-1][-1]
        
        return ans
