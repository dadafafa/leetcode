class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        dp=[[0]*(m+1) for i in range(len(A)+1)]
        for i in range(1,len(A)+1):
            for j in range(1,m+1):
                if j<A[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-A[i-1]]+A[i-1])
        return dp[len(A)][m]
        # write your code here
