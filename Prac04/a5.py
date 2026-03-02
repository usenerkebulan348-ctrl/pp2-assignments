def ronaldo_generator(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
mn=ronaldo_generator(n)
for i in mn:
    print(i)