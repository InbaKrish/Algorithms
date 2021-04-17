def kadane_largestsumarr(arr):
    maxm = arr[0]
    cur_max = 0
    start = end = s =0

    for i in range(len(arr)):
        cur_max+=arr[i]
        if cur_max > maxm:
            maxm = cur_max
            start = s
            end = i
        if cur_max<0:
            cur_max=0
            s = i+1
    #print(start,end)
    return maxm,arr[start:end+1]

print(kadane_largestsumarr([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]))