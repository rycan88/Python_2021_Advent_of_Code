import math
inp = '''target area: x=56..76, y=-162..-134'''

'''
y = int(inp[inp.index("-") + 1 : inp.index(".", inp.index("y"))])

start = (0, 0)

velocity = (11, 161)

print(sum(range(1, y)))
'''

#-----------------------------------PART 2-------------------------
count = 0
x1 = int(inp[inp.index("=") + 1: inp.index(".")])
x2 = int(inp[inp.index(".") + 2: inp.index(",")])
y1 = int(inp[inp.index("-", inp.index("-") + 1) + 1:])
y2 = int(inp[inp.index("-") + 1 : inp.index(".", inp.index("y"))])
for x in range(1, x2 + 1):
    for y in range(-y, y + 1):
        position = [0, 0]
        velocity = [x, y]
        while True:
            position[0] += velocity[0]
            position[1] += velocity[1]
            if velocity[0] > 0:
                velocity[0] -= 1
            velocity[1] += 1
            if x1 <= position[0] <= x2 and y1 <= position[1] <= y2:
                count += 1
                break
            if position[0] > x2 or position[1] > y2:
                break
print(count)
