q = [
    [0,1,6,8,8,9],
    [5,6,1,6,8,9],
    [6,5,6,1,1,9],
    [1,6,6,1,1,9],
    [6,3,3,3,3,9]
]

res = set()

for i in range(len(q)):
    for j in range(len(q[0])):
        if q[i].count(q[i][j])>3:
            res.add(q[i][j])

for i in range(len(q)-3):
    for j in range(len(q[0])):
        if q[i][j] == q[i+1][j] == q[i+2][j] == q[i+3][j]:
            res.add(q[i][j])

for i in range(len(q)-3):
    for j in range(len(q)-3):
        if q[i][j] == q[i+1][j+1] == q[i+2][j+2] == q[i+3][j+3]:
            res.add(q[i][j])

print(min(res))
