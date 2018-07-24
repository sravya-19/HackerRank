d = { '(':')', '{':'}', '[':']'}
g = int(input().strip())
for i in range(g):
  string = input()
  size = len(string)
  if size % 2 != 0:
    break
  else:
    flag = False
    for j in range(size // 2):
      if string[size - 1 - j] != d[string[i]]:
        flag = True
        break
    if flag:
      print('NO')
    else:
      print('yes')
