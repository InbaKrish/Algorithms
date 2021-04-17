s = '34567'

r = ""

for i in range(1,len(s),2):
    r+=str(int(s[i])**2)
print(r)