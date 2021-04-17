s = "dsd$^f#"
d = {}
r = ""

for i in range(len(s)):
    if not s[i].isalnum():
        d[i]=s[i]
    else:
        r+=s[i]

print(d,r)
r = list(r[::-1])
for i,j in d.items():
    r.insert(i,j)
print("".join(r))
