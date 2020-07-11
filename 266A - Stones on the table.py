numst = input()
stones = input()
arr = []
prev = ''
for x in range(len(stones)):
        if prev != stones[x]:
            arr.append(stones[x])
            prev = stones[x]
print(len(stones)-len(arr))