'''num = eval(input("Enter the pant cost : "))

if (num >= 250 and num <= 500):
    print("pant cost is budget friendly")
elif(num >= 500 and  num <= 650):
    print("pant cost is so expensive")
else:
    print("see next shop")
print("end of program")
'''

'''age = int(input("enter age in girl:"))


if(age >= 18):
    print("eligible for vote:")
elif(age <= 18):
    print(" not eligible for vote:")
else:
    print("not come for vote:")
print("stop")'''



'''num = int(input("enter a number even or odd:"))

a = " "
if(num%2 == 0):
    a += "even"
else:
    a += "odd"
print("the result is",a)'''



'''#for loop
n = int(input("Enter a number: "))

for i in range(n):
    print(i * i)

#while loop
n = int(input("entre a number:"))
i = 0

while(i<=n):
    print(i * i)
    i += 1
'''

'''n = int(input("entre the number:"))

fact = 1

for i in range(1,n+1):
    fact = fact * i
print(fact)
'''


'''
n = int(input("entre gthe value:"))

fact = 1
i = 1
while(i <= n ):
    fact = fact * i
    i = i + 1
print("Factorial =",fact)'''

'''#
n = int(input("entre the number:"))

i =1
while (i<=10):
    print(n,"x",i,"=", n*i)
    i += 1
'''

'''n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)'''




'''num = int(input("entre the number:"))
count = 0

i = 0
while(i<=num):
    if(num%1==0):
        count += 1
    i += 1

if(count == 2):
    print("prime")
else:
    print("not prime")'''


num = int(input("entre a number:"))
i = 1
sum = 0
t = num//2
while(i<= num):
    if(num%i==0):
        sum = sum + 1
        i += 1
        if(sum==num):
            print(num,"perfect number")
        else:
            print(num," not perfect number")



num = int(input("Enter a number: "))

i = 1
sum = 0

while i <= num // 2:
    if num % i == 0:
        sum = sum + i
    i += 1

if sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
