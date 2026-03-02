def ronaldo_generator(n):
    for i in range(n[0],n[1]+1):
        yield i**2
n=list(map(int,input().split()))
mn=ronaldo_generator(n)
for i in mn:
    print(i)
