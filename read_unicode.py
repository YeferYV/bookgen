'''
####### WRITE TXT ######
out1 ="(嘉南大圳 ㄐㄧㄚ　ㄋㄢˊ　ㄉㄚˋ　ㄗㄨㄣˋ )"
fobj = open("t1.txt", "w", encoding="utf-8")
fobj.write(out1)
fobj.close()

####### READ TXT #######
f = open("t1.txt", "r", encoding="utf-8").read()
print(f)
'''

def read_unicode(t1):
    file = open(t1, "r", encoding="utf-8")
    return file.read()
    file.close()

def write_unicode(t1,title):
    file = open(title, "w", encoding="utf-8")
    return file.write(t1)
    file.close()

t1="""► primera linea,
► segunda linea,
► tercera linea,
► cuarta linea,
quinta linea,
► sexta linea,
► setima linea,
► octaba linea,
► novena linea,
► decima linea,
► onceava linea,
► doceava linea"""

'''
#########GROUP OF 500 LINES#############
t1= read_unicode('► Anne_Frank.txt')
g = t1.split('\n')
h=[]
k=500
while k<=len(g):
    h+=[g[k-500:k]]
    k+=500
h+=[g[k-500:len(g)+1]]
for parrafo in range(len(h)): write_unicode('\n'.join(h[parrafo]),"Copy parrafos "+str(parrafo)+".txt")
'''

##############check if line's beginning is ► ###############3
t2= read_unicode('► Anne_Frank translated.txt')
g2= t2.split('\n')#[:1000]
for line in g2:
    #print(line[0])
    if line[0] != "►":
        print(line)



