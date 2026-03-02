def ronaldo_generator(n):
    for i in range(1,n+1):
        yield 2**i

n=int(input())
mn=ronaldo_generator(n)
for i in mn:
    print(i,end=" ")