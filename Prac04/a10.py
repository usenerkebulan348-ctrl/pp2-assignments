def ronaldo_generator(n,l):
    for i in range(l):
        for j in n:
            yield j

n=input().split()
l=int(input())
mn=ronaldo_generator(n,l)
for i in mn:
    print(i,end=" ")