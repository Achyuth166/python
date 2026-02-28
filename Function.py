#function used repeated code 
def function(n,m):
    for i in range(n):
        print(m)
function(5,"achyuth")

# function return
def name(n):
    print("achyuth")
    return n+2
print(name(5))


# multiplication table of a number
def tablet(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
tablet(19)


# adding of two numbers
#sum means result of addition of two numbers

def sum(n):
    for i in range(1,11):
        print(f"{n} + {i} = {n+i}")
sum(2)