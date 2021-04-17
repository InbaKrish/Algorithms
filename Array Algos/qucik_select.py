def partition(arr, start, end):
    pivot = start

    while start < end:
        while start < end and arr[start] <= arr[pivot]:
            start += 1
        while arr[pivot] < arr[end]:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[pivot], arr[end] = arr[end], arr[pivot]
    return end

def quick_select(arr,start,end,n):

    if start == end:
        return arr[start]
    
    pi = partition(arr,start,end)

    sub_len = pi - start + 1

    if sub_len == n:
        return arr[pi]
    if sub_len > n:
        return quick_select(arr,start,pi-1,n)
    else:
        return quick_select(arr,pi+1,end,n - sub_len)

arr =[2,8,0,14,3,1,19]
for i in range(1,len(arr)+1):
    print(quick_select(arr,0,len(arr)-1,i))
