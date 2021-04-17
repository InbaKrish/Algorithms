n = int(input())

def checkpalindrome(num):
    return str(num)==str(num)[::-1]
def reversenum(n):
    return int(str(n)[::-1])

while True:
    if checkpalindrome(n):
        break
    n +=reversenum(n)
    print(n)
print(len(str(n)))