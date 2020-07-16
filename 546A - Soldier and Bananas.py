init = input()
init = init.split()
BananaCost = int(init[0])
Money = int(init[1])
Required = int(init[2])
totalcost =0
for i in range(Required+1):
    totalcost+= BananaCost*i
if (totalcost-Money) <0:
    print(0)
else:
    print(totalcost - Money)