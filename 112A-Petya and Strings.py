import sys

str1 = input()
str2 = input()
str1=str1.upper()
str2=str2.upper()
val1 = 0
val2 =0
for x in range(len(str1)):
    if str1[x]>str2[x]:
        print(1)
        sys.exit()
    if str1[x]<str2[x]:
        print(-1)
        sys.exit()
if str1[x]==str2[x]:
    print(0)
