n=int(input())
x, y, z = map(int, input().split())
if x+y+z>n:
    print('Yes')
else:
    print('No')