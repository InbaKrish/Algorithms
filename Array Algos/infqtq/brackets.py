s = "[(((())))]["
op = ['{','[','(']
cl = ['}',']',')']
def checkparan(s):
    r = []
    for i in range(len(s)):
        if s[i] in op:
            r.append(s[i])
        elif s[i] in cl:
            id =  cl.index(s[i])
            if len(r)>0 and op[id] == r[len(r)-1]:
                r.pop()
            else:
                return (i+1)
    if len(r)==0:
        return 0
    return len(s)+1
print(checkparan(s))
