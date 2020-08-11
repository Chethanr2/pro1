n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
count = 0; sum = 0
avg = student_marks[query_name]
for i in avg:
    count = count + 1
    sum  = sum + i

val = sum / count

print("{:.2f}".format(val))