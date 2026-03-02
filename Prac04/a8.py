def ronaldo_generator(n):
    for j in range(2,n+1):
      a=True
      for i in range(2,int(j**0.5)+1):
        if j %i==0:
            a=False
            break
      if a:
        yield j
n=int(input())
mn=ronaldo_generator(n)
print(*mn)