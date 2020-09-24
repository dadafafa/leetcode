
  """       dp[i][j]表示第i个数变为j是的最小代价和，
            第i个数可以变成[0..100]内的任何一个数
            当第i个数取j的时候，第i-1个数的取值范围是[j-target,j+target] (必须在[0..100]内)
            dp[i][j] = min(dp[i][j-target], .... , dp[i][j+tagret]) + abs(A[i] - j)
  """
class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        if len(A)<=1:
            return 0
        minnum,maxnum=min(A),max(A)
        
        for i in range(len(A)):
            A[i]-=minnum
        maxnum -= minnum
        dp=[[0] * (maxnum+1) for i in range(len(A))]
        for i in range(len(A)):
            for k in range(maxnum+1):
                if i==0:
                    dp[i][k]=abs(A[i]-k)
                else:
                    min_predp=max(0,k-target)
                    max_predp=min(maxnum,k+target)
                    dp[i][k]=min(dp[i-1][min_predp:max_predp+1])+abs(A[i]-k)

        
        # print(dp)    
        return min(dp[len(A)-1])
        
        # write your code here
