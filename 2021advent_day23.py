import math

inp = '''#############
#...........#
###D#D#B#A###
  #B#C#A#C#
  #########'''

dots = inp.count(".")

Order = []
for x in inp:
    if x in "ABCD":
        Order.append(x)

Spaces = set()
for x in range(dots):
    Spaces.add((x, 0))

Rooms = []
for y in range(1, 3):
    for x in range(2, 9, 2):
        Spaces.add((x, y))
        Rooms.append((x, y))

Current = []
Box = []
for x in range(ord("A"), ord("D") + 1):
    i = Order.index(chr(x))
    Box.append(Rooms[i])
    Box.append(Rooms[Order.index(chr(x), i + 1)])

def AddTup(x, y):
    return (x[0] + y[0], x[1] + y[1])

def Move(State, i, direction):
    return State[:i] + [AddTup(State[i], direction)] + State[i + 1:]

def recursion(State, energy):
    for i in range(8):
        piece = State[i]



Around = ((1, 0), (0, 1), (-1, 0), (0, -1))
Box = tuple(Box)
D = {}
D[Box] = 0

# I ENDED UP DOING THIS DAY BY HAND
print("I ENDED UP DOING THIS DAY BY HAND")
