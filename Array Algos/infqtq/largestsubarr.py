l = [
    [1,0,1,1,0], 
    [1,1,1,1,1], 
    [1,0,1,1,1], 
    [1,1,1,1,1]
]

for i in range(1,len(l)):
    for j in range(1,len(l[0])):
        if l[i][j]==0:
            continue
        else:
            s = min(l[i-1][j-1],l[i-1][j],l[i][j-1])
            l[i][j]+=s

print(max(list(map(max,l))))
