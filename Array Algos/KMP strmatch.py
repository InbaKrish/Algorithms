def computeLPS(lps,pat):
    l = 0
    i=1 

    while i<len(pat):
        if pat[l]==pat[i]:
            lps[i] = l+1
            l+=1
            i+=1
        else:
            if l!=0:
                l = lps[l-1]
            else:
                lps[i]=0
                i+=1

def KMP(txt,pat):
    #pat = pat.lower()
    #txt = txt.lower()
    res =[]
    lps = [0]*len(pat)
    computeLPS(lps,pat)

    i=j=0
    
    while i< len(txt):
        if txt[i]==pat[j]:
            i+=1
            j+=1
        else:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1
        if j==len(pat):
            res.append(i-j)
            j=lps[j-1]
    return res


print(KMP('AABAACAADAABAABA', 'AABA'))
