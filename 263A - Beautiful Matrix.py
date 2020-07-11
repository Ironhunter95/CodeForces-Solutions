r1 = str(input())
r2 = str(input())
r3 = str(input())
r4 = str(input())
r5 = str(input())
r1 =''.join(r1.split())
r2 =''.join(r2.split())
r3 =''.join(r3.split())
r4 =''.join(r4.split())
r5 =''.join(r5.split())
A = [r1, r2, r3, r4,  r5]
row = 0
column = 0
newx = 0
newy = 0
for x in range(0, 5):
    for y in range(0, 5):
        if int(A[x][y]) == 1:
            row = x+1
            column = y+1
            break
if row > 3:
    newx = row-3
elif row < 3:
    newx = 3-row
if column > 3:
    newy = column-3
elif column < 3:
    newy = 3-column
print(newx+newy)