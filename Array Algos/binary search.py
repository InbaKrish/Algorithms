def BinarySearch(arr,l,u,key):
    if l<=u:
        mid = (l+u)//2
        if key == arr[mid]:
            return True
        else:
            if key<arr[mid]:
                return BinarySearch(arr,l,mid-1,key)
            else:
                return BinarySearch(arr,mid+1,u,key)
    else:
        return False


l = [1, 4, 8, 12, 23, 45, 60]
print(BinarySearch(l,0,len(l)-1,3))
    
