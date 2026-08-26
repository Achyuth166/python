'''name = "Achyuth"
college = "avm"
fee = 90000
bus = 20000
auto = 20.7
branch = "cse"'''

'''print(f"my name is :{name} ")
print(f"college name is :{college} ")
print(f"college fee is :{fee} ")
print(f"bus fee is : {bus} ")
print(f"auto fee is :{auto}")
print(f"branch is :{branch} ")'''



''' #type of variable
print(type(name))
print(type(college))
print(type(fee))
print(type(bus))
print(type(auto))
print(type(branch))'''


# operators
#types of operators
#arithmetic operators(+,-,*,/)
#relational operators(>,<,>=,<=,==,!=)
#assignment operators(=,+=,-=,*=,/=)
#logical operators(and,or,not)


'''a = 10
b = 30
print(a+b)#40
print(a-b)#-20
print(a*b)#300
print(a/b)#0.3333333333333333'''





'''#relational operators(>,<,>=,<=,==,!=)
a = 30
b = 10
print(a > b)  
print(a < b)  
print(a >= b)  
print(a!= b) # a!=b a is not equal to b or =!  this symbol not valid in python 
print(a == b) # a==b a is equal to b'''






'''# assignment operators(=,+=,-=,*=,/=)
a = 15
b = 15.9
print(a == b)
print(a = b)
print(a*=b)
print(a/=b)
# above code wornge
#print() expects a value or expression, not an assignment.

# this code is correct 
# Assignment operators (=, +=, -=, *=, /=)

a = 15
b = 15.9

print(a == b)    # Comparison

a = b
print(a)

a *= b
print(a)

a /= b
print(a)'''




'''# logical operators (and, or, not)

#and → Both must be True
#or → At least one must be True
#not → Changes True to False, and False to True

print(10 < 5 and 20 > 10)   # True
print(10 > 5 or 20 < 10)    # True
print(not(10 > 5))          # False'''


'''print("Hello", "World", 5, "endl", 2)
print("Hello")
print(" World!")
print(1,2,3,4,5)
print("I love CodeChef")
print(10-3)'''


'''a = "10 20"
b = a.split()
c = map(int, b)
print(list(c))
# same code 
a = "11 22"
print(list(map(int, a.split())))


a = "aa bb"
print(list(map(str, a.split())))
# sAME CODE TOP AND BOTTOM
a = "aa bb"
b = a.split()
c = map(str,b)
print(list(c))'''


'''text = "1 2 3"
print(list(map(int,text.split())))

a, b = 2, 4
a,b= (map(int,input().split()))
print(a,b)'''



x,y = 10 ,30
print(x+1,y-3)

