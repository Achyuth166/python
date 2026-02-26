# modules
k = [3,4,5,6,7,8,12,16,2,6,8,]
ans = 0
for i in k:
    if i % 7 == 0:
        ans = ans + 1
print(ans)

# "and" operator both side correct it will be excuted in if conditions
# "or" operator one side correct it will be excuted either if or else  conditions


p = [2,4,6,8,3,6,9]
ans = 0
for i in p:
    if i % 2 == 0 and i % 3 == 0:
        ans = ans + 1
print(ans)


s = [3,6,8,9,5,2]
ans = 0
for i in s:
    if i % 2 == 0 or i % 3 == 0:
        ans = ans + 1
print(ans)