lines = int(input())
final = 0
for x in range(lines):
    inp = input()
    if '+' in inp:
        final+=1
    else:
        final-=1
print(final)