import math
from collections import defaultdict

inp = '''CKFFSCFSCBCKBPBCSPKP

NS -> P
KV -> B
FV -> S
BB -> V
CF -> O
CK -> N
BC -> B
PV -> N
KO -> C
CO -> O
HP -> P
HO -> P
OV -> O
VO -> C
SP -> P
BV -> H
CB -> F
SF -> H
ON -> O
KK -> V
HC -> N
FH -> P
OO -> P
VC -> F
VP -> N
FO -> F
CP -> C
SV -> S
PF -> O
OF -> H
BN -> V
SC -> V
SB -> O
NC -> P
CN -> K
BP -> O
PC -> H
PS -> C
NB -> K
VB -> P
HS -> V
BO -> K
NV -> B
PK -> K
SN -> H
OB -> C
BK -> S
KH -> P
BS -> S
HV -> O
FN -> F
FS -> N
FP -> F
PO -> B
NP -> O
FF -> H
PN -> K
HF -> H
VK -> K
NF -> K
PP -> H
PH -> B
SK -> P
HN -> B
VS -> V
VN -> N
KB -> O
KC -> O
KP -> C
OS -> O
SO -> O
VH -> C
OK -> B
HH -> B
OC -> P
CV -> N
SH -> O
HK -> N
NO -> F
VF -> S
NN -> O
FK -> V
HB -> O
SS -> O
FB -> B
KS -> O
CC -> S
KF -> V
VV -> S
OP -> H
KN -> F
CS -> H
CH -> P
BF -> F
NH -> O
NK -> C
OH -> C
BH -> O
FC -> V
PB -> B'''

'''

B = inp.split("\n\n")

D = {}
for x in B[1].split("\n"):
    D[x[:2]] = x[-1]


Seq = B[0]
for turns in range(10):
    NewSeq = ""
    for x in range(len(Seq) - 1):
        NewSeq += Seq[x]
        pair = Seq[x: x + 2]
        if pair in D:
            NewSeq += D[pair]
    NewSeq += Seq[-1]
    Seq = NewSeq

Count = []
for x in set(D.values()):
    Count.append(Seq.count(x))
print(max(Count) - min(Count))
'''

# ------------------------------------------------PART 2---------------------------

B = inp.split("\n\n")

Pairs = defaultdict(int)
Letters = {}
D = {}
for x in B[1].split("\n"):
    D[x[:2]] = x[-1]
    Pairs[x[:2]] = 0
    Letters[x[-1]] = 0

Seq = B[0]
for x in range(len(Seq) - 1):
    pair = Seq[x: x + 2]
    Pairs[pair] += 1
    Letters[Seq[x]] -= 1
Letters[Seq[0]] += 1



for turns in range(40):
    NewPairs = defaultdict(int)
    for pair in Pairs:
        if pair in D:
            let = D[pair]
            NewPairs[pair[0] + let] += Pairs[pair]
            NewPairs[let + pair[1]] += Pairs[pair]
            Letters[let] -= Pairs[pair]
        else:
            NewPairs[pair] += Pairs[pair]
    Pairs = NewPairs.copy()
for pair in Pairs:
    Letters[pair[0]] += Pairs[pair]
    Letters[pair[1]] += Pairs[pair]

Count = Letters.values()
print(max(Count) - min(Count))


