inp = '''3,5,3,1,4,4,5,5,2,1,4,3,5,1,3,5,3,2,4,3,5,3,1,1,2,1,4,5,3,1,4,5,4,3,3,4,3,1,1,2,2,4,1,1,4,3,4,4,2,4,3,1,5,1,2,3,2,4,4,1,1,1,3,3,5,1,4,5,5,2,5,3,3,1,1,2,3,3,3,1,4,1,5,1,5,3,3,1,5,3,4,3,1,4,1,1,1,2,1,2,3,2,2,4,3,5,5,4,5,3,1,4,4,2,4,4,5,1,5,3,3,5,5,4,4,1,3,2,3,1,2,4,5,3,3,5,4,1,1,5,2,5,1,5,5,4,1,1,1,1,5,3,3,4,4,2,2,1,5,1,1,1,4,4,2,2,2,2,2,5,5,2,4,4,4,1,2,5,4,5,2,5,4,3,1,1,5,4,5,3,2,3,4,1,4,1,1,3,5,1,2,5,1,1,1,5,1,1,4,2,3,4,1,3,3,2,3,1,1,4,4,3,2,1,2,1,4,2,5,4,2,5,3,2,3,3,4,1,3,5,5,1,3,4,5,1,1,3,1,2,1,1,1,1,5,1,1,2,1,4,5,2,1,5,4,2,2,5,5,1,5,1,2,1,5,2,4,3,2,3,1,1,1,2,3,1,4,3,1,2,3,2,1,3,3,2,1,2,5,2'''

'''
L = list(map(int, inp.split(",")))

D = {}
for x in range(9):
    D[x] = L.count(x)

D2 = {}
for days in range(80):
    for x in range(8):
        D2[x] = D[x + 1]
    D2[8] = D[0]
    D2[6] += D[0]
    D = D2.copy()
print(sum(D.values()))
'''

#----------------------------------PART 2----------------------------

L = list(map(int, inp.split(",")))

D = {}
for x in range(9):
    D[x] = L.count(x)

D2 = {}
for days in range(256):
    for x in range(8):
        D2[x] = D[x + 1]
    D2[8] = D[0]
    D2[6] += D[0]
    D = D2.copy()
print(sum(D.values()))