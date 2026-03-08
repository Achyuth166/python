r = 3
c = 3
for i in range(r):
    for j in range(c):
        print("*", end="")
        if j != c-1:
            print("-", end=" ")
    print()

#example 1
r = 3
c = 10
for i in range(r):
    for j in range(c):
        print("*", end="")
        if j != c-1:
            print("-", end=" ")
    print()

#example 2
r = 7
c = 3
for i in range(r):
    for j in range(c):
        print("*", end="")
        if j != c-1:
            print("-", end=" ")
    print()

#example 3
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
'''


'''r = 5
c = 4
for i in range(r):
    for j in range(c):
        if i == 0 or j == 0 or i == r-1 or j == c-1:
            print("*", end="")
        else:
            print(" ", end="")
            
        if j != c-1:
            print(" ", end="")
    print()'''

'''r = 4
c = 15
for i in range(r):
    for j in range(c):
        if i == 0 or j == 0 or i == r-1 or j == c-1:
            print("*", end="")
        else:
            print(" ", end="")

        if j != c-1:
            print(" ", end=" ")
    print()'''


'''#example
r = 16
c= 5
c1 = r-1
for i in range(r):
    for j in range(c1-i):
        print(" ", end="")
    for k in range(c):
        print("*", end="")
    print()



r = 16
c= 5
c1 = r-1
for i in range(r):
    for j in range(i):
        print(" ", end="")
    for k in range(c):
        print("*", end="")
    print()'''

#examples
r = 6
c = 5
c1 = r-1
for i in range(r):
    for j in range(c1 - i):
        print("-", end="")
    

