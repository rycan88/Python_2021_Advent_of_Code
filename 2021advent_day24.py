import math

inp = '''inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 16
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -9
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 16
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -2
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -16
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y'''


# a, b, c
# [a, 1, a + 15, a + 15]
# [b, 1, a + 15, (a + 15) * 27]

def Process(string):
    Scores = [0, 0, 0, 0]
    count = 0
    for line in L:
        mode = line[0]
        i = ord(line[1]) - ord("w")
        if mode == "inp":
            Scores[i] = int(string[count])
            count += 1
        else:
            if line[2] in LETTERS:
                value = Scores[ord(line[2]) - ord("w")]
            else:
                value = int(line[2])

            if mode == "add":
                Scores[i] += value
            elif mode == "mul":
                Scores[i] *= value
            elif mode == "div":
                Scores[i] = int(Scores[i] / value)
            elif mode == "mod":
                Scores[i] %= value
            elif mode == "eql":
                if Scores[i] == value:
                    Scores[i] = 1
                else:
                    Scores[i] = 0
    return Scores

def SmallEnough(equation):
    for letter in string:
        for x in range(1, 17):
            if equation == "( " + letter + " + " + str(x) + " )":
                return True
            if equation == "( " + str(x) + " + " + letter + " )":
                return True
    return False

def ReplaceAll(s, string1, string2):
    turn = 0
    while string1 in s:
        turn += 1
        s = s.replace(string1, string2)
    print(turn)
    return s

L = inp.split("\n")


I = []
for x in range(len(L)):
    L[x] = L[x].split()

LETTERS = ("w", "x", "y", "z")

string = ""
for x in range(ord("a"), ord("a") + 14):
    string += chr(x)

minimum = math.inf

Score = Process()

'''Scores = ["0", "0", "0", "0"]
count = 0
for line in L:
    mode = line[0]
    i = ord(line[1]) - ord("w")
    if mode == "inp":
        Scores[i] = string[count]
        count += 1
        if count == 5:
            break
    else:
        if line[2] in LETTERS:
            value = Scores[ord(line[2]) - ord("w")]
        else:
            value = line[2]

        Type= [-1, -1]
        if Scores[i] in string:
            Type[0] = "string"
        elif "(" in Scores[i]:
            Type[0] = "equation"
        else:
            Type[0] = "number"

        if value in string:
            Type[1] = "string"
        elif "(" in value:
            Type[1] = "equation"
        else:
            Type[1] = "number"

        if mode == "add":
            if Scores[i] == "0":
                Scores[i] = value
            elif value == "0":
                continue
            elif Type == ["number", "number"]:
                Scores[i] = str(int(Scores[i]) + int(value))
            else:
                Scores[i] = "( " + Scores[i] + " + " + value + " )"
        elif mode == "mul":
            if "0" in (Scores[i], value):
                Scores[i] = "0"
            elif Scores[i] == "1":
                Scores[i] = value
            elif value == "1":
                continue
            elif Type == ["number", "number"]:
                Scores[i] = str(int(Scores[i]) * int(value))
            else:
                Scores[i] = "( " + Scores[i] + " * " + value + " )"
        elif mode == "div":
            if Scores[i] == "0":
                continue
            elif value == "1":
                continue
            elif Type == ["number", "number"]:
                Scores[i] = str(int(int(Scores[i]) + int(value)))
            else:
                Scores[i] = "( " + Scores[i] + " / " + value + " )"
        elif mode == "mod":
            if Scores[i] == "0":
                continue
            elif Type == ("number", "number"):
                Scores[i] = str(int(Scores[i]) % int(value))
            elif SmallEnough(Scores[i]):
                continue
            else:
                Scores[i] = "( " + Scores[i] + " % " + value + " )"
        elif mode == "eql":

            if Type[0]  == "string" and Type[1] == "number" and (int(value) < 1 or int(value) > 9):
                Scores[i] = "0"
            elif Type[0] == "number" and Type[1] == "string" and (int(Scores[i]) < 1 or int(Scores[i]) > 9):
                Scores[i] = "0"
            elif Type[0] == "number" and Type[1] == "number":
                Scores[i] = str(int(int(Scores[i]) == int(value)))
            elif Type[0] == "equation" and (Type[1] == "string" or value == "0"):
                if "/" not in Scores[i] and "%" not in Scores[i] and "==" not in Scores[i] and "+" in Scores[i]:
                    for a in range(10, 27):
                        if "+ " + str(a) in Scores[i]:
                            Scores[i] = "0"
                    if Scores[i] == "0":
                        continue
                    else:
                        Scores[i] = "( " + Scores[i] + " == " + value + " )"
            else:
                Scores[i] = "( " + Scores[i] + " == " + value + " )"


answer = Scores[3]

#answer = ReplaceAll(answer, )
print(answer)'''


