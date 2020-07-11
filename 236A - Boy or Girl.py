name = input()
arr, letters = [], []
dchars = 0
for x in range(len(name)):
    if name[x] not in arr:
        arr.append(name[x])
        dchars +=1
if dchars % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
