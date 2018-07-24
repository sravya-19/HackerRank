n = int(input())
li = list(map(int, input().strip().split()))
print(sum([li.count(i) // 2 for i in set(li)]))
