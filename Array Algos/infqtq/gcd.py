def naivegcd(a,b):
    if a>b:
        small = b
    else:
        small = a
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            gcd = i

    print(gcd)

def algobased(a,b):
    while(b):
        a,b = b,a%b
    print(a)

algobased(60,48)