s = "5u6@25g7#@"

e = 0
even,odd = [],[]
for i in s:
    if not i.isalnum():
        e+=1
    if i.isdigit():
        if int(i)%2==0:
            even.append(int(i))
        else:
            odd.append(int(i))
      

if e%2==0:
    pass
else:
    even,odd = odd,even

print(even,odd)
if len(even) > len(odd):
    for i in range(len(odd)):
        print(f"{even[i]}{odd[i]}", end="")
    for i in even[len(odd):]:
        print(i, end="")
else:
    for i in range(len(even)):
        print(f"{even[i]}{odd[i]}", end="")
    for i in odd[len(even):]:
        print(i, end="")
