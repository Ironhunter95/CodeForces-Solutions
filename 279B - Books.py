line1 = input()
line2 = input()
line1 = line1.split()
line2 = line2.split()
numOfBooks = line1[0]
freeTime = line1[1]
arr=[]
read=0
t1, t2 = 0, 0
print("Number of Books:",numOfBooks,"Free Time:",freeTime)
for i in range(len(line2)):
    arr.append(line2[i])
#arr.sort()
freeTime = int(freeTime)
for x in arr:
    if freeTime>int(x) or freeTime==int(x):
        print("Current Free Time:",freeTime,"Current Book time:",x)
        freeTime = freeTime-int(x)
        read+=1
    elif freeTime<int(x):
        break
print(read)