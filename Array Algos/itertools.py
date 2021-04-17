import itertools

a = [23,24,25,26,27]
'''l = [*enumerate(a)]
print(l)

#count runs like a for loop 
s = list(zip(itertools.count(),a))
print(s)  # [(0, 23), (1, 24), (2, 25), (3, 26), (4, 27)]

#zip_longest zips the longest iterable passed even though the smallest ends with the none
t = list(itertools.zip_longest(range(10),a))
print(t)  #[(0, 23), (1, 24), (2, 25), (3, 26), (4, 27), (5, None), (6, None), (7, None), (8, None), (9, None)]

#cycle - cycles through the given iterable thing
r = itertools.cycle([1,2,3])
for i in range(8):
    print(next(r),end=" ")
print()

#repeat
squares = list(map(pow,range(11),itertools.repeat(2)))
print(squares)

#starmap - iters thorugh paired tuples instead of lists
sq = list(itertools.starmap(pow, [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]))
print(sq)'''

#QUITE USEFOOL TOOLS
l = ['a','b','c','d']

#combinations - provides the possible combinations in the iterable passed in which oreder doesnt matters
r = itertools.combinations(l,2)
print(list(r))

#permutations - provides the possible combinations in the iterable passed in which order matters
r = itertools.permutations(l,2)
print(list(r))

#product - it also similar to permutaions but it aloows repeating same iter values to be repeated
r = itertools.product([0,1,2],repeat=3)
print(list(r))

#to allow repeat in combinations the below method can be used
r = itertools.combinations_with_replacement([0,1,2],3)
print(list(r))

#chain method combines multiple iterables into one
l = [0,1,2,3]
s = ['a','b','c']
r = itertools.chain(l,s)
print(list(r))