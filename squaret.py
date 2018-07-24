size = int(input())
list1 = list(map(int, input().split(' ')))
test = int(input())
for t in range(test):
    q = int(input())
    summer = 0
    for i in range(size):
        summer += list1[i]
        if summer >= q:
            print(i + 1)
            break
    print(-1)
