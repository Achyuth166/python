# array loo unna elements i loo ki repeat ayithayi.
# In case array loo 3 elements untey 3 times print ayithayi.

# syntax
# for i in range(6):
#   print(i)

# for loop arry call chesthey n-1 varaku print chesthayi.
# suppose array loo 3 elements untey 0,1,2 print chesthayi.

# one time excuted in loop
k = ["bhavani", "bhanu", "teja"]
for i in k:
    print(i)


# number of types excuted in loop
k = ["bhavani", "bhanu", "teja"]
for name in k:
    for i in range(3):
        print(name)

# suppose array loo 3 elements untey 3 times print ayithayi.
g = ["achyuth", "sai"] 
for name  in g:
    for i in range(5):
        print(name)

# countin in ones in array
li = [1,2,44,5,3,6,1,1,1,7,8,99,0,1]
n = len(li)
ans = 0
for i in range(n):
    if li[i] == 1:
        ans = ans + 1
print(ans)