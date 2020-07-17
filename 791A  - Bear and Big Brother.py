weights = input()
weights = weights.split()
Limak = int(weights[0])
Bob = int(weights[1])
c = 0
for i in range(10):
    Limak = Limak * 3
    Bob  = Bob *2
    c+=1
    if Limak > Bob:
        print(c)
        break