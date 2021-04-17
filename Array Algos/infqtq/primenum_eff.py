from math import sqrt
import time
def find_prime(n):
    if n<=1:
        return False
    if n>=4 and ((n%2==0) or (n%3==0)):
        return False
    else:
        k = 1
        a,b = 6*k+1,6*k-1
        while b<=int(sqrt(n)):
            if n%a==0 or n%b==0:
                return False
            k+=1
            a, b = 6*k+1, 6*k-1
    return True

# start = time.time()
# for i in range(1000):
#     if find_prime(i):
#         print(i,end=" ,")
# print('\n',time.time()-start)


start = time.time()
for i in range(1000):
    f=1
    if i>1:
        j=2
        while j*j<=i:
            if i%j==0:
                f=0
                break
            j+=1
        if(f):
            print(i,end=" ,")
print('\n', time.time()-start)

#print(list(filter(lambda X:X,[0,1,4,5,0,9])))

#print(find_prime(25))

