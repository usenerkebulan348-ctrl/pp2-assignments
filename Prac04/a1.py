def ronaldo_generator(n):
    for i in range(0,n+1):

        yield i**2

n=int(input())
mn=ronaldo_generator(n)
for i in mn:
    
        print(i)


