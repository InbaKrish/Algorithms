""" 
eg : 29953 -> 29954 29955 29956 29957 29958 29959 (7) -> 29960 => 2996
     2996 -> 2997 2998 2999 (4) -> 3000 => 3
     3 -> 4 5 6 7 8 9 1 2
"""
n = "29953"
i = len(n)-1
total = 0
carry = 0
while i>0:
    cur = 10 - (int(n[i])+carry)
    carry = 1
    total += cur
    i-=1
total += 9
print(total)