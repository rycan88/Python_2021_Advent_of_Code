import math
inp = '''[[[0,[6,6]],[[7,2],[6,2]]],[[[9,4],[5,8]],6]]
[[[4,9],6],[[[0,1],[8,5]],[3,[7,6]]]]
[[1,7],[[[1,3],2],[[6,8],8]]]
[4,[[6,[6,0]],[[4,9],5]]]
[[3,8],[[0,6],1]]
[[2,2],[[[2,3],[2,9]],[[9,6],[4,9]]]]
[[[3,4],[[7,7],[7,8]]],[[0,2],6]]
[[[[4,4],[3,3]],[[9,0],4]],[8,[7,[6,6]]]]
[[[9,9],8],1]
[2,[[7,[1,9]],[9,2]]]
[[[[6,0],[8,2]],[[9,0],[8,7]]],[3,[6,[8,8]]]]
[[[8,[9,2]],[1,4]],[[2,2],[[1,0],5]]]
[[[9,[0,3]],[4,[2,3]]],[[8,[0,1]],[[4,8],[5,4]]]]
[[[2,0],[1,7]],[[3,[0,7]],[[7,6],0]]]
[[[1,[5,1]],[[0,3],9]],[[3,8],[[5,3],1]]]
[[[[4,5],2],[[7,7],[4,8]]],[3,[3,[6,5]]]]
[[[[4,4],4],[[5,0],2]],[9,[[0,7],5]]]
[[2,[[8,0],9]],0]
[[[[0,5],[1,0]],[0,[5,1]]],[[[0,8],[6,0]],[6,[3,9]]]]
[[[[2,4],[5,5]],[4,7]],[[[5,6],[9,5]],1]]
[[[4,[5,1]],[[6,7],1]],[1,[[5,9],4]]]
[[0,6],[[9,3],[4,2]]]
[7,[[[2,4],[3,4]],[2,0]]]
[0,[6,7]]
[[[0,2],[[7,2],7]],[[[6,3],[2,0]],[[8,6],[7,9]]]]
[[[7,[0,5]],7],[[2,3],[3,3]]]
[[2,[0,[4,5]]],[[4,[7,9]],[[5,6],4]]]
[[[5,4],0],[5,[[7,1],[7,6]]]]
[[0,3],[[[5,2],5],[[8,5],[2,8]]]]
[[[0,[8,9]],[[3,1],2]],[[3,[7,1]],7]]
[[[[9,7],[5,5]],[[2,4],1]],[[1,3],[[4,0],[9,1]]]]
[[[0,9],4],0]
[[[[8,8],9],[[8,2],3]],[[2,[7,4]],[9,1]]]
[[[1,2],8],[[[4,4],2],[2,4]]]
[[6,[7,[2,1]]],[[2,1],3]]
[0,[[[7,8],0],[5,[8,5]]]]
[[[2,8],6],[6,[[1,1],[1,2]]]]
[[[[3,9],2],[7,[4,9]]],[[[5,3],3],[[7,3],5]]]
[[2,[4,[3,2]]],[[4,9],6]]
[[[[1,1],[0,5]],[1,[4,9]]],[[6,[5,7]],[[1,6],[7,2]]]]
[0,[0,[[8,5],8]]]
[[[1,[2,5]],8],[[3,[0,2]],4]]
[[[4,3],0],[[[6,9],[7,2]],[[1,9],8]]]
[[[[7,1],0],[7,5]],[6,2]]
[[[9,[6,5]],6],[[5,5],[[4,6],2]]]
[[[[3,0],[5,5]],2],[7,[9,[8,5]]]]
[9,[[9,7],[3,3]]]
[[[0,0],4],[7,[[5,8],[2,7]]]]
[[[[9,2],4],[[0,1],[4,1]]],[[4,[6,5]],5]]
[8,[[[5,2],8],[6,0]]]
[[[[9,6],2],9],[5,[[5,3],5]]]
[[[8,[8,0]],[7,[3,3]]],[[[8,8],[5,5]],[[1,3],3]]]
[[[2,3],4],[[[8,8],[1,4]],5]]
[[[[3,7],9],6],[[5,[4,1]],4]]
[[[3,4],[[5,3],4]],[[2,[4,2]],[[0,7],5]]]
[0,9]
[[2,[[9,1],[3,4]]],[[[5,7],[6,6]],[5,[3,6]]]]
[[[[7,2],7],[[8,7],9]],[9,[[7,0],[3,4]]]]
[[[[8,3],[0,2]],0],[5,[[9,9],1]]]
[[[1,5],[[3,9],[5,6]]],[6,[2,[2,4]]]]
[[[[1,6],7],[8,9]],[[[6,7],8],1]]
[[5,[[1,3],[1,8]]],[8,1]]
[[[[4,6],9],[[3,0],[2,4]]],3]
[[[[6,6],[9,8]],[4,7]],[[6,8],1]]
[[[9,[7,8]],[4,[0,3]]],[[8,[8,1]],8]]
[4,0]
[[[[1,8],[6,9]],[[1,5],[6,1]]],[[1,9],[0,1]]]
[[[[1,8],[1,8]],[[6,2],[8,6]]],[[[6,8],3],[[8,0],[7,3]]]]
[8,9]
[[2,8],2]
[[4,[[7,0],[1,8]]],1]
[[5,0],[[[3,4],0],3]]
[[[[7,5],2],6],[[9,2],[[5,0],[7,5]]]]
[[8,[[0,0],[3,7]]],[1,6]]
[[[[5,2],[5,1]],[8,6]],[2,[9,[5,4]]]]
[[[6,[3,3]],[[0,4],0]],[[4,4],[[3,6],6]]]
[[7,[[4,9],[9,7]]],[3,[[8,7],9]]]
[[[[3,3],9],[8,[7,2]]],[[3,9],8]]
[[[0,[9,2]],1],[6,[[9,7],8]]]
[[5,[0,1]],[8,7]]
[[[[0,7],5],8],[[[0,0],[7,1]],[2,[6,9]]]]
[[5,[[3,3],7]],[[[1,3],[5,4]],[[0,8],[2,2]]]]
[[[[7,4],5],[[9,1],[5,5]]],[[0,8],[0,[6,4]]]]
[[0,[[9,5],[4,3]]],[[[2,7],[4,7]],6]]
[[7,[[3,2],[7,9]]],[[[8,6],[1,8]],[5,[5,6]]]]
[[0,[[3,3],0]],[[[5,2],[2,4]],[6,8]]]
[[[6,[5,6]],9],[[[5,2],7],[[8,7],[2,4]]]]
[[[[7,2],[8,2]],5],[[[4,5],[0,7]],6]]
[[[[6,1],4],6],[[4,[7,8]],3]]
[[[[2,6],[5,0]],5],[[3,[5,4]],[[2,3],[8,6]]]]
[[4,[[1,3],[1,3]]],[[[5,1],2],[[7,3],[9,6]]]]
[[8,[6,[0,0]]],[[[4,4],9],[6,2]]]
[[9,7],7]
[[[3,1],[[0,3],[5,2]]],3]
[[1,5],[4,[0,[3,6]]]]
[[[[4,9],[6,5]],[8,4]],2]
[[[7,[1,5]],4],[[3,[4,6]],[7,[4,3]]]]
[[[0,[5,7]],[[8,7],[2,6]]],[[4,5],5]]
[[[2,3],[[9,5],[9,3]]],[[[2,5],9],[[9,1],8]]]
[[[[4,4],4],[[4,0],9]],[[[5,3],1],[3,[7,6]]]]'''




'''
def NextNum(string, i): #Put the last index
    start = ""
    end = ""
    s = ""
    for x in range(i + 1, len(string)):
        if string[x] not in CHARACTERS:
            start = x
            s += string[x]
            x += 1
            while x < len(string) and string[x] not in CHARACTERS:
                s += string[x]
                x += 1
            end = x #ONE ABOVE THE END
            break
    return s, start, end

def PrevNum(string, i):
    start = ""
    end = ""
    s = ""
    for x in range(i, -1, -1):
        if string[x] not in CHARACTERS:
            end = x + 1
            s = string[x] + s
            x -= 1
            while x >= 0 and string[x] not in CHARACTERS:
                s = string[x] + s
                x -= 1
            start = x + 1 #ONE ABOVE THE END
            break
    return s, start, end



def Explode(string):
    brac_count = 0
    index = ""
    for i in range(len(string)):
        if string[i] == "[":
            brac_count += 1
        elif string[i] == "]":
            brac_count -= 1
        if brac_count == 5:
            index = i
            break

    if index == "":
        return string

    comma = string.index(",", index)
    close_b = string.index("]", index)
    pair = (int(string[index + 1: comma]), int(string[comma + 1: close_b]))
    nextnum, start, end = NextNum(string, close_b)
    if nextnum != "":
        string = string[:start] + str(pair[1] + int(nextnum)) + string[end:]
    string = string[:index] + "0" + string[close_b + 1:]
    index -= 1
    prevnum, start, end = PrevNum(string, index)
    if prevnum != "":
        string = string[:start] + str(pair[0] + int(prevnum)) + string[end:]
    return string

def Split(string):
    i = 0
    while True:
        s, start, end = NextNum(string, i)
        if s == "":
            return string
        num = int(s)
        if num >= 10:
            pair = "[" + str(math.floor(num / 2)) + "," + str(math.ceil(num / 2)) + "]"
            string = string[: start] + pair + string[end :]
            return string
        else:
            i = end
    return string

def Magnitude(string):
    start = -100
    end = -100
    while "[" in string:
        for i in range(len(string)):
            if string[i] == "[":
                start = i
            elif string[i] == "]":
                end = i
                comma = string.index(",", start)
                pair = (int(string[start + 1: comma]), int(string[comma + 1: end]))
                string = string[:start] + str(3 * pair[0] + 2 * pair[1]) + string[end + 1:]
                break
    return string
L = inp.split("\n")
CHARACTERS = ("[", ",", "]")
answer = L[0]
for x in range(1, len(L)):
    line = "[" + answer + "," + L[x] + "]"
    while True:
        newline = Explode(line)
        if newline == line:
            newline = Split(line)
            if newline == line:
                break
        line = newline
    answer = line

print(Magnitude(answer))
'''

# ----------------------------------PART 2-------------------


def NextNum(string, i): #Put the last index
    start = ""
    end = ""
    s = ""
    for x in range(i + 1, len(string)):
        if string[x] not in CHARACTERS:
            start = x
            s += string[x]
            x += 1
            while x < len(string) and string[x] not in CHARACTERS:
                s += string[x]
                x += 1
            end = x #ONE ABOVE THE END
            break
    return s, start, end

def PrevNum(string, i):
    start = ""
    end = ""
    s = ""
    for x in range(i, -1, -1):
        if string[x] not in CHARACTERS:
            end = x + 1
            s = string[x] + s
            x -= 1
            while x >= 0 and string[x] not in CHARACTERS:
                s = string[x] + s
                x -= 1
            start = x + 1 #ONE ABOVE THE END
            break
    return s, start, end



def Explode(string):
    brac_count = 0
    index = ""
    for i in range(len(string)):
        if string[i] == "[":
            brac_count += 1
        elif string[i] == "]":
            brac_count -= 1
        if brac_count == 5:
            index = i
            break

    if index == "":
        return string

    comma = string.index(",", index)
    close_b = string.index("]", index)
    pair = (int(string[index + 1: comma]), int(string[comma + 1: close_b]))
    nextnum, start, end = NextNum(string, close_b)
    if nextnum != "":
        string = string[:start] + str(pair[1] + int(nextnum)) + string[end:]
    string = string[:index] + "0" + string[close_b + 1:]
    index -= 1
    prevnum, start, end = PrevNum(string, index)
    if prevnum != "":
        string = string[:start] + str(pair[0] + int(prevnum)) + string[end:]
    return string

def Split(string):
    i = 0
    while True:
        s, start, end = NextNum(string, i)
        if s == "":
            return string
        num = int(s)
        if num >= 10:
            pair = "[" + str(math.floor(num / 2)) + "," + str(math.ceil(num / 2)) + "]"
            string = string[: start] + pair + string[end :]
            return string
        else:
            i = end
    return string

def Magnitude(string):
    start = -100
    end = -100
    while "[" in string:
        for i in range(len(string)):
            if string[i] == "[":
                start = i
            elif string[i] == "]":
                end = i
                comma = string.index(",", start)
                pair = (int(string[start + 1: comma]), int(string[comma + 1: end]))
                string = string[:start] + str(3 * pair[0] + 2 * pair[1]) + string[end + 1:]
                break
    return string
L = inp.split("\n")
CHARACTERS = ("[", ",", "]")

biggest = 0
for answer in L:
    for string in L:
        if answer == string:
            continue
        line = "[" + answer + "," + string + "]"
        while True:
            newline = Explode(line)
            if newline == line:
                newline = Split(line)
                if newline == line:
                    break
            line = newline
        biggest = max(biggest, int(Magnitude(line)))
print(biggest)

