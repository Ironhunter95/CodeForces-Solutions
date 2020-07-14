name = input()
arr, letters = [], []
dchars = 0
ls =0
ans=""
for x in range(len(name)):
    if name[x] != 'l':
        if name[x] not in arr:
            arr.append(name[x])
            dchars +=1
    elif name[x] == 'l':
        if ls<2:
            arr.append(name[x])
            ls+=1
for x in range(len(arr)):
    ans += arr[x]
if ans.__contains__("hello"):
    print("YES")
else:
    print("NO")