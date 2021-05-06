
arr = [10,2,4,8,0,1,9,7]
m = 4
rems = {}

for i in arr:
    cur_rem = i%m
    if cur_rem not in rems:
        rems[cur_rem] = 1
    else:
        rems[cur_rem]+=1
    
print(rems)

ans = 0

for key in rems:
    pairs = 0
    d = m - key
    if d == m or (2*d == m):
        pairs = (rems[key]*(rems[key]-1))//2
    elif d in rems:
        pairs = rems[key]*rems[d]
        rems[key]=0
    ans+=pairs
print(ans)