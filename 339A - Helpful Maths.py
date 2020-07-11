eq = input()
eq2 = eq.replace('+', '')
testlist = []
fn =''
for x in eq2:
    testlist.append(int(x))
tl2=sorted(testlist)
for y in tl2:
    fn+=str(y) + '+'
fn = fn[:-1]
print(fn)