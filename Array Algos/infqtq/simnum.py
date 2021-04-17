'''l = "3,2,6,5,1,4,8,9"

l = list(map(int,l.split(",")))

fiv = l.index(5)
ei = l.index(8)
ans = 0
print(fiv,ei)

ans+=sum(l[:fiv])
print(l[:fiv+1])
ans+=sum(l[ei+1:])
print(l[ei+1:])

s = list(map(str, l[fiv:ei+1]))
print(s)
ans+=int("".join(s))

print(ans)'''

s = "1023422"

a = []
for i in s:
    if i.isdigit() and int(i) not in a:
        a.append(int(i))
a.sort(reverse=True)
print(a)

for i in range(len(a)-1,0,-1):
    if a[i] ==0:
        mineven = 0
        break
    elif a[i]%2==0:
        mineven = a[i]
        break
if mineven%2!=0:
    print(-1)
else:
    a.remove(mineven)
    print(a,mineven)

#print(0%0)
    
