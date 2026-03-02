def ronaldo_generator(n):
    for i in range(1,n+1):
        if i %2==0:
            yield i
n=int(input())
mn=ronaldo_generator(n)
for i in mn:
    if i==n or i==n-1:
        print(i)
    else:
        print(i,end=" ")