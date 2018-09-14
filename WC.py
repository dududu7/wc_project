import os

import sys, re


def digui(path1, a, type1):
    pathDir = os.listdir(path1)
    if a == 1:
        path1 += "/"
    for allDir in pathDir:
        newDir = os.path.join('%s%s' % (path1, allDir))
        #print(newDir)
        #print('111\t', os.path.splitext(newDir)[1])
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".py":
                read(newDir, type1)
                pass
            if os.path.splitext(newDir)[1] != ".py":
                pass
        else:
            digui(newDir, 1, type1)




# 列表检索一次返回多个位置（index一次只能返回第一个找到的）
def find(file):
    tar = ('\'\'\'\n')
    return [i for (i, v) in enumerate(file) if v == tar]


# 数出word，注释行
def count_word(file, symbol, Zhu):
    # 拼接正则表达式
    symbol = "[" + symbol + "]+"
    word = re.split(symbol, file)
    Length = len(word)
    Zhu += file.count('#')

    return Length, Zhu


# 数出char,line,Empty_line,Code_line,一部分注释行
def count_cl(file):
    P = len(file)
    Empth_L = file.count('\n')
    num_zhu = file.count('\'\'\'\n')
    Empth_L += num_zhu
    C = file.__sizeof__()
    Code = P - Empth_L

    if num_zhu > 0:
        place = find(file)
    # print("place", place, type(place),num_zhu)
    Zhu = 0
    for i in range(1, int(num_zhu / 2) + 1):
        # print('1',place[2 * i - 1],'-',place[2*i-2])
        Zhu += place[2 * i - 1] - place[2 * i - 2] - 1

    return P, C, Empth_L, Code, Zhu


def print1(P, Length, C, Empth_L, Zhu, Code, type1):
    if type1 == "-l":
        print("行数：\t", P)
    if type1 == "-w":
        print("单词数：\t", Length)
    if type1 == "-c":
        print("字符数：\t", C)
    if type1 == "-a":
        print("空行数为：\t", Empth_L)
        print("注释行数为：\t", Zhu)
        print("代码行数为：\t", Code)


def read(file, type1):
    symbol = '!@#$%^&*()-+=:"[]{},.\n '  # 排除掉各种其他的符号
    with open(file, 'r', encoding='gb18030', errors='ignore') as Re:  # 'r'为读取而打开，为默认模式,出现中文无法识别时，用ignore忽略，不过中文读取时会变成乱码
        file = Re.readlines()
    P, C, Empth_L, Code, Zhu = count_cl(file)
    file = ' '.join(file)
    Length, Zhu = count_word(file, symbol, Zhu)
    print1(P, Length, C, Empth_L, Zhu, Code, type1)


def menu():
    print("目录：  1_NULL.py\t空文件\n\t1_word.py\t一个字母\n\t1st.py\t一行代码\n\t1_F.py；WC.py\t完整代码")


def main():
    type1 = input("请输入参数： \n\t-c  -char\n\t-w  -word\n\t-l  -line\n\t-a  高级选项\n\t-s  递归输出结果\n\t")

    if type1 == "-s":
        type1 = input("请输入递归参数：")
        print(type1)
        digui(r"C:/Users/Administrator/Desktop/Python/", 0, type1)  # 不在路径前加r会报错
        pass
    else:
        menu()
        name = input("请输入文件:")
        read(name, type1)

main()