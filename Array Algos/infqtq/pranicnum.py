s = "4567"
res = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
print(res)
def pranic(s):
    ans = []
    for i in range(len(s)-1):
        mul = int(s[i])*int(s[i+1])
        if str(mul) in res:
            ans.append(mul)
    if len(ans)==0:
        print("-1")
    else:
        print(ans)

pranic(s)