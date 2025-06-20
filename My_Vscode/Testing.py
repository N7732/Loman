import itertools
L=[1,2,3]
K=[4,6,8]
Sum=[]
for i,j in itertools.zip_longest(L,K,fillvalue=0):
    Sum.append(i+j)
print(Sum)