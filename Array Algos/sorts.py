def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j],arr[j+1] = key,arr[j]
            j-=1
    return arr

def bubble_sort(arr):
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if not swap:
            break

def merge(a1,a2,arr):
    i = j = k = 0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            arr[k] = a1[i]
            i+=1
        else:
            arr[k] = a2[j]
            j+=1
        k+=1
    
    while i<len(a1):
        arr[k]=a1[i]
        k+=1
        i+=1
    while j<len(a2):
        arr[k]=a2[j]
        k+=1
        j+=1

def merge_sort(arr):
    if len(arr)>1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        merge_sort(left)
        merge_sort(right)

        return merge(left,right,arr)
    else:
        return 

def partition(arr,start,end):
    pivot = start

    while start<end:
        while start<end and arr[start] <= arr[pivot]:
            start+=1
        while arr[pivot]<arr[end]:
            end-=1
        if start<end:
            arr[start],arr[end]= arr[end],arr[start]
    
    arr[pivot],arr[end] = arr[end],arr[pivot]
    return end

def quick_sort(arr,start,end):
    if start<end:
        pi = partition(arr,start,end)
        quick_sort(arr,0,pi-1)
        quick_sort(arr,pi+1,end)

arr =[2,8,0,14,3,1,19]
quick_sort(arr,0,len(arr)-1)
print(arr)