
inp = '''Player 1 starting position: 2
Player 2 starting position: 5'''

'''
P = inp.split("\n")
p1 = int(P[0][-2:]) - 1
p2 = int(P[1][-2:]) - 1
Points = [0, 0]
steps = 0 # One less than times rolled
while True:
    running = False
    for x in range(3):
        p1 += (steps % 100) + 1
        steps += 1

    Points[0] += (p1 % 10) + 1
    if Points[0] >= 1000:
        break
    for x in range(3):
        p2 += (steps % 100) + 1
        steps += 1

    Points[1] += (p2 % 10) + 1
    if Points[1] >= 1000:
        break

if Points[0] < 1000:
    print(Points[0] * steps)
else:
    print(Points[1] * steps)
'''
# ----------------------------------PART 2-----------------

def recursion(p11, p22, P, m):
    global count
    for i in range(len(Steps)):
        p1 = p11

        multiplier = m
        Points = P.copy()
        p1 += Steps[i]
        Points[0] += (p1 % 10) + 1
        multiplier *= Ways[i]
        if Points[0] >= 21:
            Wins[0] += multiplier
            continue
        for ii in range(len(Steps)):
            multiplier2 = multiplier
            Points2 = Points.copy()
            p2 = p22
            p2 += Steps[ii]
            Points2[1] += (p2 % 10) + 1
            multiplier2 *= Ways[ii]
            if Points2[1] >= 21:
                Wins[1] += multiplier2
                continue
            recursion(p1, p2, Points2, multiplier2)

P = inp.split("\n")

Wins = [0, 0]
Steps = (3, 4, 5, 6, 7, 8, 9)
Ways = (1, 3, 6, 7, 6, 3, 1)

p1 = int(P[0][-2:]) - 1
p2 = int(P[1][-2:]) - 1
Points = [0, 0]
multiplier = 1
recursion(p1, p2, Points, multiplier)
print(max(Wins))

