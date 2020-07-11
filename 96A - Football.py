players = input()
T = 1
i=0
for x in players:
    if i == (len(players)-1):
        break
    if players[i+1] == players[i]:
        T=T+1
        if T>5:
            print("YES")
            break
    else:
        T=0
    i+=1
if T<6:
    print("NO")