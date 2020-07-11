numOfLines = int(input())
x, y, z =[], [], []
for i in range(numOfLines):
    value = input()
    value = value.split()
    x.append(int(value[0]))
    y.append(int(value[1]))
    z.append(int(value[2]))
if sum(x) == 0 & sum(y) == 0 & sum(z) == 0:
    print("YES")
else:
    print("NO")