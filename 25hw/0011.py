n=int(input())
x = list(map(int, input().split()))
x.remove(max(x))
print(max(x))