def naive_substr(txt,pat):

    res = []
    for i in range(len(txt)-len(pat)+1):
        j = 0

        while j<len(pat):
            if txt[i+j]!=pat[j]:
                break
            j+=1
        
        if j==len(pat):
            res.append(i)
    return res

print(naive_substr('abefcdef','ef'))