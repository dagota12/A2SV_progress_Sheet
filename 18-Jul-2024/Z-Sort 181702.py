# Problem: Z-Sort - https://codeforces.com/problemset/problem/652/B

n = int(input())
arr = [int(i) for i in input().split()]
 
arr.sort()
res = []
p1,p2 = 0,len(arr) - 1
turn = True
for i in range(n):
    if turn:
        turn = False
        res.append(arr[p1])
        p1+=1
    else:
        turn = True
        res.append(arr[p2])
        p2-=1
 
print(*res)