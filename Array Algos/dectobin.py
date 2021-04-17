count = 0
def dectobin(n):
    if n>=1:
        dectobin(n//2)
    print(n%2,end="")
    globals()['count'] += n%2

dectobin(7)
print('\n',count)
# n = 24
# while n>=1:
#     print(n%2)
#     n = n//2