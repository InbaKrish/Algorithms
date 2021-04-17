# l = [[40, 42, 2,],
# [30, 24, 27],
# [180, 190 ,40],
# [11, 121 ,13]]

# ans = []

# for i in range(1,len(l)):
#     for j in range(1,len(l)):
#         if l[i][j] % sum(list(str(l[i][j]))) == 0 and l[i-1][j] % sum(list(l[i-1][j])) == 0 and l[i][j-1] % sum(list(l[i][j-1])) == 0 and l[i-1][j-1] % sum(list(l[i-1][j-1])) == 0:
#             res = [[0]*2]*2
#             res[1, 1] = l[i][j]
#             res[0, 0] = l[i-1][j-1]
#             res[0, 1] = l[i-1][j]
#             res[1,0] = l[i][j-1]
#             ans. append(res)
# print(ans)

def fib(n,dp):
    if n<=1:
        dp[n]=n
        return n
    else:
        if dp[n-1]!=-1:
            return dp[n-1]
        else:
            a = fib(n-1,dp)
            b = fib(n-2,dp)
            dp[n]=a+b
            return dp[n]

dp  = [-1]*6
print(dp)
print(fib(6,dp))
print(dp)