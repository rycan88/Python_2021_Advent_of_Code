import math

inp = '''820D4A801EE00720190CA005201682A00498014C04BBB01186C040A200EC66006900C44802BA280104021B30070A4016980044C800B84B5F13BFF007081800FE97FDF830401BF4A6E239A009CCE22E53DC9429C170013A8C01E87D102399803F1120B4632004261045183F303E4017DE002F3292CB04DE86E6E7E54100366A5490698023400ABCC59E262CFD31DDD1E8C0228D938872A472E471FC80082950220096E55EF0012882529182D180293139E3AC9A00A080391563B4121007223C4A8B3279B2AA80450DE4B72A9248864EAB1802940095CDE0FA4DAA5E76C4E30EBE18021401B88002170BA0A43000043E27462829318F83B00593225F10267FAEDD2E56B0323005E55EE6830C013B00464592458E52D1DF3F97720110258DAC0161007A084228B0200DC568FB14D40129F33968891005FBC00E7CAEDD25B12E692A7409003B392EA3497716ED2CFF39FC42B8E593CC015B00525754B7DFA67699296DD018802839E35956397449D66997F2013C3803760004262C4288B40008747E8E114672564E5002256F6CC3D7726006125A6593A671A48043DC00A4A6A5B9EAC1F352DCF560A9385BEED29A8311802B37BE635F54F004A5C1A5C1C40279FDD7B7BC4126ED8A4A368994B530833D7A439AA1E9009D4200C4178FF0880010E8431F62C880370F63E44B9D1E200ADAC01091029FC7CB26BD25710052384097004677679159C02D9C9465C7B92CFACD91227F7CD678D12C2A402C24BF37E9DE15A36E8026200F4668AF170401A8BD05A242009692BFC708A4BDCFCC8A4AC3931EAEBB3D314C35900477A0094F36CF354EE0CCC01B985A932D993D87E2017CE5AB6A84C96C265FA750BA4E6A52521C300467033401595D8BCC2818029C00AA4A4FBE6F8CB31CAE7D1CDDAE2E9006FD600AC9ED666A6293FAFF699FC168001FE9DC5BE3B2A6B3EED060'''

'''
def foo(i):
    global string, total
    version = int(string[i: i + 3], 2)
    id = int(string[i + 3: i + 6], 2)
    total += version
    i += 6
    if id == 4:
        while True:
            if string[i] == "0":
                i += 5
                break
            else:
                i += 5
    else:
        if string[i] == "0":
            i += 1
            package_length = int(string[i: i + 15], 2)
            i += 15
            while package_length > 0:
                new_i = foo(i)
                package_length -= new_i - i
                i = new_i
        else:
            i += 1
            num_of_packages = int(string[i: i + 11], 2)
            i += 11
            for x in range(num_of_packages):
                new_i = foo(i)
                i = new_i
    return i


string = bin(int(inp, 16))[2:]
while (len(string) % 4) != 0:
    string = "0" + string
total = 0
i = 0
foo(i)
print(total)
'''

#----------------------------------------------PART 2--------------

def foo(i):
    global string
    version = int(string[i: i + 3], 2)
    id = int(string[i + 3: i + 6], 2)
    i += 6
    if id == 4:
        s = ""
        while True:
            s += string[i + 1: i + 5]
            if string[i] == "0":
                i += 5
                break
            else:
                i += 5
        value = int(s, 2)
    else:
        Values = (0, 1, math.inf, 0 , None, -1, -1, -1)
        value = Values[id]
        if string[i] == "0":
            i += 1
            package_length = int(string[i: i + 15], 2)
            i += 15
            while package_length > 0:
                new_i, new_value = foo(i)
                if id == 0:
                    value += new_value
                elif id == 1:
                    value *= new_value
                elif id == 2:
                    value = min(value, new_value)
                elif id == 3:
                    value = max(value, new_value)
                elif id == 5:
                    if value == -1:
                        value = new_value
                    else:
                        value = (value > new_value)
                elif id == 6:
                    if value == -1:
                        value = new_value
                    else:
                        value = (value < new_value)
                elif id == 7:
                    if value == -1:
                        value = new_value
                    else:
                        value = (value == new_value)
                package_length -= new_i - i
                i = new_i
        else:
            i += 1
            num_of_packages = int(string[i: i + 11], 2)
            i += 11
            for x in range(num_of_packages):
                new_i, new_value = foo(i)
                if id == 0:
                    value += new_value
                elif id == 1:
                    value *= new_value
                elif id == 2:
                    value = min(value, new_value)
                elif id == 3:
                    value = max(value, new_value)
                elif id == 5:
                    if value == -1:
                        value = new_value
                    else:
                        value = (value > new_value)
                elif id == 6:
                    if value == -1:
                        value = new_value
                    else:
                        value = (value < new_value)
                elif id == 7:
                    if value == -1:
                        value = new_value
                    else:
                        value = (value == new_value)
                i = new_i
    return i, value


string = bin(int(inp, 16))[2:]
for x in inp:
    if x == "0":
        string = "0000" + string
    else:
        break
while (len(string) % 4) != 0:
    string = "0" + string

i = 0
i, value = foo(i)
print(value)

