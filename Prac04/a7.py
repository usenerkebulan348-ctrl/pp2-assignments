def ronaldo_generator(n):
    for i in n[::-1]:
        yield i 
n=input()
mn=ronaldo_generator(n)
for i in mn:
    print(i,end=" ")