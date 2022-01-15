
inp = '''he-JK
wy-KY
pc-XC
vt-wy
LJ-vt
wy-end
wy-JK
end-LJ
start-he
JK-end
pc-wy
LJ-pc
at-pc
xf-XC
XC-he
pc-JK
vt-XC
at-he
pc-he
start-at
start-XC
at-LJ
vt-JK'''

'''
L = inp.split("\n")

D = {}
S = set()
for x in range(len(L)):
    L[x] = L[x].split("-")
    first = L[x][0]
    second = L[x][1]
    if first not in S:
        S.add(first)
        D[first] = set()
    if second not in S:
        S.add(second)
        D[second] = set()

    D[first].add(second)
    D[second].add(first)

Box = [["start"]]
count = 0
while len(Box) > 0:
    NewBox = []
    for seq in Box:
        for adj in D[seq[-1]]:
            if adj == adj.lower() and adj in seq:
                continue
            if adj == "end":
                count += 1
            else:
                NewBox.append(seq + [adj])
    Box = []
    for x in NewBox:
        Box.append(x[:])
print(count)
'''

L = inp.split("\n")

D = {}
S = set()
for x in range(len(L)):
    L[x] = L[x].split("-")
    first = L[x][0]
    second = L[x][1]
    if first not in S:
        S.add(first)
        D[first] = set()
    if second not in S:
        S.add(second)
        D[second] = set()

    D[first].add(second)
    D[second].add(first)

Box = [["start"]]
count = 0
while len(Box) > 0:
    NewBox = []
    for seq in Box:
        for adj in D[seq[-1]]:
            if adj == "start":
                continue
            if adj == adj.lower() and adj in seq:
                if 0 not in seq:
                    NewBox.append([0] + seq + [adj])
                continue
            if adj == "end":
                count += 1
            else:
                NewBox.append(seq + [adj])
    Box = []
    for x in NewBox:
        Box.append(x[:])
print(count)


