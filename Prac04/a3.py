def ronaldo_generator(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
mn=ronaldo_generator(n)
for i in mn:
    print(i,end=" ")