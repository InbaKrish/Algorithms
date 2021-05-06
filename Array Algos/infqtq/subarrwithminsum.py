""" Given array of n elements ,, we need to find the subarr of size m , whose sum is minimum"""

def possible_k(arr,m,k):
    cur_sum = arr[0]
    subs = 1
    flag = True
    for i in range(1,len(arr)):
        if cur_sum + arr[i] > k:
            cur_sum = arr[i]
            subs+=1
        else:
            cur_sum+=arr[i]
        if subs>m:
            flag = False
            break
    return flag

arr = [1,2,3,4,5]
m = 3

left = max(arr)
right = sum(arr)
mid = (left+right)//2
ans = []
while left<=right:
    if possible_k(arr,m,mid):
        ans.append(mid)
        right = mid-1
    else:
        left = mid+1
    mid = (left+right)//2
print(min(ans))
        
