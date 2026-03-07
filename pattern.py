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
