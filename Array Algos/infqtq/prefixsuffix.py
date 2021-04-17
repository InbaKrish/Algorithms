def lps(a,s):
    i = 0
    j = 1
    while j<len(s):
        if s[i]==s[j]:
            i += 1
            a[j]=i
            j += 1
        else:
            if i!=0:
                i = a[i-1]
            else:
                a[i]=0
                j+=1
    res = a[len(s)-1]
    if res>len(s)/2:
        print(a[len(s)//2])
    else:
        print(res) 

s = "wwwwwwww"
l = [0]*len(s)
lps(l,s)
