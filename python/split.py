
from os import close


if __name__ == "__main__" :
    f = open("PeaceSheep/2/train_100w.txt","r",encoding='utf8')
    i = 100000
    file_num = 1
    file = open("PeaceSheep/2/"+str(file_num)+".txt","w",encoding='utf8')
    last_line = ''
    for line in f.readlines():
        if last_line != '\n' and last_line !='' and line != '\n':
            i-=1
            file.write(last_line)
            file.write(line)
            if i == 0 :
                file.close()
                file_num+=1
                file = open("PeaceSheep/2/"+str(file_num)+".txt","w",encoding='utf8')
                i=100000
        last_line = str(line)