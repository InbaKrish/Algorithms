def checkperfect(num):
    s = 1
    i = 2
    while i**2<=num:
        if num%i==0:
            s+=i+num//i
        i+=1
    return s==num

def checkarmstrng(n):
    s = 0
    num = n
    while num>0:
        digit = num%10
        print(digit)
        s+=digit**3
        print(s)
        num = num//10
    return s==n

# for i in range(1000):
#     if checkarmstrng(i):
#         print(i,end=" ,")

print(checkarmstrng(407))
