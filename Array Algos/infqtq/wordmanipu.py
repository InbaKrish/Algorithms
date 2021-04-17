s = 'HelLoWOrld'
l = sorted(set(s.upper()))
print(l)
res = []
for i in range(len(l)):
    n = ""
    for j in s:
        if l[i]==j.upper():
            n+=j
    res.append(n)
print(res)
i = 0
j = len(res)- 1
ans = ""
while i<=j:
    if i==j:
        ans+=res[i]
    else:
        ans+=res[i]+res[j]
    i+=1
    j-=1
print(ans)
