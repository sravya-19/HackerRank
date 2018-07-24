def solve(grades):
	for i in range(len(grades)):
		if grades[i] >= 38:
			if (grades[i] + 1) % 5 == 0:
				grades[i] += 1
			elif (grades[i] + 2) % 5 == 0:
				grades[i] += 2
	return(grades)


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
