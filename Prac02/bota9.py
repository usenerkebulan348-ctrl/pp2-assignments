a=int(input())
b=list(map(int,input().split()))
c=max(b)
m=min(b)
for i in range(a):
    if b[i] == c:
        b[i]=m
print(*b)