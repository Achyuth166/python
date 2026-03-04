p = "s"
print(ord(p))

i = "r"
print(ord(i))

n = "i"
print(ord(n))

e = "n"
print(ord(e))

a = "u"
print(ord(a))

#leetcode problems
class Solution:
    def scoreOfString(self, s: str) -> int:

        ans = 0
        for i in range(len(s)-1):
            a = ord(s[i])
            b = ord(s[i+1])
            temp = abs(a-b)
            ans = ans + temp

        return ans
    

li = ["--X","X++","++X","X++","++X"]
x = 0
for i in li:
    if i == "--X" or i == "X--":
        x = x - 1
    else:
        x = x + 1
    
return x




s = "1.1.1"
ans = ""
for i in s:
    if i == ".":
        ans = ans + "[.]"
    else:
        ans = ans + i
print(ans)