# python
# -*- coding:
'''        if C > 1000:
            f1 = ' '.join(file[:l])
            Length = count_word(f1, symbol)
            file = ' '.join(file[l:])
            Length += count_word(file, symbol)

        else:
        '''

import os

def digui(path1,a):
    pathDir = os.listdir(path1)
    if a == 1 :
        path1 += "/"
    for allDir in pathDir:
        newDir = os.path.join('%s%s' % (path1, allDir))
        print(newDir)
        print('111\t',os.path.splitext(newDir)[1])
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".py":
                 with open(newDir,encoding='gb18030',errors='ignore') as file:
                     print(file.read())
                 pass
            if os.path.splitext(newDir)[1] != ".py":
                 pass
        else:
             digui(newDir,1)

digui(r"C:/Users/Administrator/Desktop/Python/",0)