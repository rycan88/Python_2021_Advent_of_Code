
inp = '''7777838353
2217272478
3355318645
2242618113
7182468666
5441641111
4773862364
5717125521
7542127721
4576678341'''

'''
def AddTup(x, y):
    return (x[0] + y[0], x[1] + y[1])

L = inp.split("\n")

D = {}
AROUND = ((1, 0), (1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, -1), (-1, 1))
for y in range(len(L)):
    for x in range(len(L[0])):
        D[(x,y)] = int(L[y][x])

total = 0
for turns in range(100):
    Found = set()
    Box = []
    for x in D:
        D[x] += 1
        if D[x] > 9:
            Box.append(x)
            Found.add(x)
    while len(Box) > 0:
        NewBox = []
        for coord in Box:
            for around in AROUND:
                newtup = AddTup(coord, around)
                if newtup in D and newtup not in Found:
                    D[newtup] += 1
                    if D[newtup] > 9:
                        NewBox.append(newtup)
                        Found.add(newtup)
        Box = NewBox
    total += len(Found)
    for x in Found:
        D[x] = 0
print(total)
'''

def AddTup(x, y):
    return (x[0] + y[0], x[1] + y[1])

L = inp.split("\n")

D = {}
AROUND = ((1, 0), (1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, -1), (-1, 1))
for y in range(len(L)):
    for x in range(len(L[0])):
        D[(x,y)] = int(L[y][x])
OCT_NUM = len(D)
turns = 0
while True:
    turns += 1
    Found = set()
    Box = []
    for x in D:
        D[x] += 1
        if D[x] > 9:
            Box.append(x)
            Found.add(x)
    while len(Box) > 0:
        NewBox = []
        for coord in Box:
            for around in AROUND:
                newtup = AddTup(coord, around)
                if newtup in D and newtup not in Found:
                    D[newtup] += 1
                    if D[newtup] > 9:
                        NewBox.append(newtup)
                        Found.add(newtup)
        Box = NewBox
    if len(Found) == OCT_NUM:
        break
    for x in Found:
        D[x] = 0
print(turns)

