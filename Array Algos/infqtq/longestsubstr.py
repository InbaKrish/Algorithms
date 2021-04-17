s = "BBBB"
r = []

for i in range(len(s)-1):
    sub = s[i]
    for j in range(i+1,len(s)):
        if s[j]!=s[i] and s[j] not in sub:
            sub+=s[j]
        else:
            r.append(sub)
            break
    if not r:
        r.append(sub)

print(r)
print(1%2)