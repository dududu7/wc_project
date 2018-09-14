
from optparse import OptionParser

def opt():
    pa = OptionParser()
    option,args = pa.parse_args()
    return option,args
    


def count(file,symbol):
    P = file.count('\n')
    
#拼接正则表达式
    symbol = "["+ symbol + "]+"
    word = re.split(symbol,file)
    Length = len(word)
    C = len(file)
     
    return P,Length,C


def print1(P,Length,C,type1):
    if type1 == "-l":
        print(P)
    elif type1 == "-w":
        print(Length)
    else:
        print(C)



def main():
    print("第一步：\n目录：  1_NULL.py\t空文件\n\t1_word.py\t一个字母\n\t1_Line.py\t一行代码\n\t1_F.py\t完整代码")
    type1 = input("请输入参数： \n\t-c  -char\n\t-w  -word\n\t-l  -line\n")
    numble = input("请输入文件:")  	   
    #dict1 = {'0':'D:\py_file\Test_NULL.py','1':'D:\py_file\Test_word.py','2':'D:\py_file\Test_P.py','3':'D:\py_file\Test_F.py','4':'game_guess-random.py'}
    #with open(dict1[numble],"r") as Re:
    
    with open(numble,'r') as Re:    	    	#为读取而打开，可以不写
        file = Re.readlines()
        print(type(file))
    file = ' '.join(file)
                                                #文件内容以字符串形式存入file  比起Re = open(dict1[numble])之后close文件要好
                                            	#file = Re.read() 容易超出字符串上限，所以改成逐行读取的方法,
    symbol = '!@#$%^&*()-+=, '  	    	    #排除掉各种其他的符号
    P,Length,C = count(file,symbol)
    print1(P,Length,C,type1)
    print(file)
             



             


main()

