'''def nthnum(n):
    result = 0
    p = 1

    while n > 0:
        result += (p*(n % 9))
        n = n//9
        p *= 10
    return result


swap = 0
def partition(arr, start, end):
    pivot = start

    while start < end:
        # start searches for larger element thans pivot
        while start < len(arr) and arr[start] <= arr[pivot]:
            start += 1
        while arr[end] > arr[pivot]:  # end searches for smaller element than pivot
            end -= 1
        if start < end:  # swaps start and end at end
            arr[end], arr[start] = arr[start], arr[end]
            globals()['swap']+=1

    arr[pivot], arr[end] = arr[end], arr[pivot]
    globals()['swap']+=1

    return end

def quick_sort(arr, start, end):
    if start < end:
        # gets the swapped indexed , centre of two partitions
        pivot_index = partition(arr, start, end)
        quick_sort(arr, 0, pivot_index-1)
        quick_sort(arr, pivot_index+1, end)

arr = [45,23,12,68,50,39,48]
quick_sort(arr,0,len(arr)-1)
print(swap,arr)'''

def find_min_Swaps(l):
    n = len(l)
    arrpos = [*enumerate(l)]
    arrpos = sorted(arrpos,key=lambda pos:pos[1])

    visit = {k : False for k in range(n)}
    result = 0

    for i in range(n):

        if visit[i] or arrpos[i][0] == i:
            continue

        cycle = 0
        j = i

        while not visit[j]:
            visit[j] = True
            j = arrpos[j][0]
            cycle+=1
    
    result+=cycle
    return cycle


def rec(n):
    if n>0:
        print(n)
        rec(n-1)

def fib(n):
    l = [0,1]
    x,y = l
    if n<0:
        return False
    elif n==1:
        return 1
    else:
        for i in range(2,n):
            n = x+y
            l.append(n)
            x,y = y,n
    return l


def designerPdfViewer(h, word):
    #print(h)
    #l = [h[ord(i)%97] for i in word]

    return max([h[ord(i) % 97] for i in word])*len(word)*1

def checkcount(arr1,arr2):
    res = []
    for i in arr2:
        res.append(arr1.count(i))
    print(res)

def primeprint(a,b):

    for i in range(a,b+1):
        f = 0
        if i>1:
            j = 2
            while j*j<=i:
                if(i%j)==0:
                    f=1
                    break
                j+=1
            if f==0:
                print(i)


def majority(arr):
    ma = {}
    for i in arr:
        if i not in ma:
            ma[i] = 1
        else:
            ma[i]+=1
    print(max(ma))

#checkcount(['ab','abc','ab'],['ab','abc','de'])
#primeprint(1,36)
majority([1,1,1,1,1,4,5])
#print(designerPdfViewer("1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7".split(),"zaba"))

# l = [1, 5, 4, 3, 2]
# print(find_min_Swaps(l))
#rec(9)
