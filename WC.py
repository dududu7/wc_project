import os

import sys, re


def digui(path1, type1):
    path1 = path1.replace(r"\\", "\\")
    #print(path1)
    pathDir = os.listdir(path1)
    if not os.path.isdir(path1):
        print("Wrong Path！")
        exit()
    path1 += "\\"
    for allDir in pathDir:
        newDir = os.path.join('%s%s' % (path1, allDir))
        print(newDir)
        #print('111\t', os.path.splitext(newDir)[1])
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".py":
                read(newDir, type1)
                pass
            if os.path.splitext(newDir)[1] != ".py":
                pass
        else:
            digui(newDir, type1)




# 列表检索一次返回多个位置（index一次只能返回第一个找到的）
def find(file):
    tar = ('\'\'\'\n')
    return [i for (i, v) in enumerate(file) if v == tar]


# 数出word，注释行
#数出word，注释行
def count_word(file,symbol,Zhu):
#拼接正则表达式
    symbol = "["+ symbol + "]+"
    word = re.split(symbol,file)
    Length = len(word)
    Zhu += file.count('#')
    #print(word)

    return Length,Zhu
# 数出char,line,Empty_line,Code_line,一部分注释行
def count_cl(file):
    P = len(file)
    Empth_L = file.count('\n')
    num_zhu = file.count('\'\'\'\n')
    Empth_L += num_zhu
    Code = P - Empth_L
    if num_zhu > 0:
        place = find(file)
    Zhu = 0
    for i in range(1, int(num_zhu / 2) + 1):
        Zhu += place[2 * i - 1] - place[2 * i - 2] - 1
    return P, Empth_L, Code, Zhu

#    输出
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
    if type1 == "-h":
        print("行数：\t\t", P)
        print("单词数：\t", Length)
        print("字符数：\t", C)
        print("空行数为：\t", Empth_L)
        print("注释行数为：\t", Zhu)
        print("代码行数为：\t", Code)



def read(file, type1):

    with open(file, 'r', encoding='gb18030', errors='ignore') as Re:  # 'r'为读取而打开，为默认模式,出现中文无法识别时，用ignore忽略，不过中文读取时会变成乱码
        Fill = Re.read()
    with open(file, 'r', encoding='gb18030', errors='ignore') as Re:
        file = Re.readlines()
    C = len(Fill)
    P,  Empth_L, Code, Zhu = count_cl(file)
    symbol = '~!@#$%^&*(\\t)_+{}\t:=\\-"<>?/.,\'\\n '  # 排除掉各种其他的符号
    Length, Zhu = count_word(Fill, symbol, Zhu)
    print1(P, Length, C, Empth_L, Zhu, Code, type1)


def main():
    type1 = input("请输入参数后回车： \n\t-c  -char\n\t-w  -word\n\t-l  -line\n\t-a  高级选项\n\t-s  递归输出结果\n\t-h  输出全部结果\n")
    if type1 == "-s":
        type1 = input("请输入递归参数：")
        path = input("请输入路径：")
        print(type1)
        digui(path, type1)
        pass
    elif type == "-c" or "-w" or "-l" or "-a" or "-h":
        name = input("请输入文件路径:")
        read(name, type1)
    else :
        print("wrong input!")
        exit()
main()