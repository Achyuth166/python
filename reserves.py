s = "Achyuth"
for i in range(6,-1,-1,):
    print(s[i])
print(len(s))# length of string

k = [5,8,9,1,0]
for i in range(4,-1,-1):
    print(k[i]) 


g = "aba"
for i in range(2,-1,-1):
    print(g[i]) 



h = "abcd"
ans = ""
for i in range(3,-1,-1):
    ans = ans + h[i]
if (ans == h):
    print("Palindrome")
else:
    print("Not a palindrome")
# code indexing gives in string changes


g = "dog"
ans = ""
for i in range(len(g)-1,-1,-1):
    ans = ans + g[i]
if (ans == g):
    print("yes,Palindrome")
else:
    print("Not a palindrome")
    # correctly working code for palindrome check
