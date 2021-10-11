#from bookgen import *

#t=input("""""").split()          #lee un parrafo
def leer2():                      #lee parrafos txt
    archivo1=open("alicia en el pais de las maravillas.txt","r")
    return archivo1.read()
    archivo1.close()
t2=leer2().split()

#input:  ['hola mundo de tiempo']
#output: ['hola mundo de tiempo.']
def addpoint(t):
    l=[]
    for k in t:
        if k[-1]!=".":
            k+="."
        #l.append(k) == l+=[k]      != l+=k
        l+=[k]
    #return readstring(l)
    return l
#print(addpoint(["hola mundo de tiempo."]))

def delpoint(t):
    l=[]
    for k in t:
        if k[-1]==".":
            k=k[:-1]
        l+=[k]
    #return readstring(l)
    return l

#input:  ['hola'],['mundo'],['de'],['tiempo']
#output:  'hola mundo de tiempo.'
def readstring(l):
    n=""
    for k in l:
        n+=k+" "
    return n
#print(readstring(addpoint(t)))

def digito_repetido_2(l):
    #l=list(str(l))
    #m=l[:]
    #m=list(str(l))
    l=str(l)
    for k in range(len(l)):
        m=l[:k]+l[k+1:]         #equivale a "m=l[:]" "x=m[k]" "del m[k]" "m[k:k]=x"
        #x=m[k]
        #del m[k]
        for j in range(len(m)):
            if l[k]==m[j]:
                print(l[k], 'si se repite')
        #m[k:k]=x
#print(digito_repetido_2(12321))

def delete(l,p):
    #l[p:p]=["hola"]           #insert
    #l[p:p+1]=["hola"]         #replace l[p]="hola"
    return l[:p]+l[p+1:]       #delete
#print(delete([2,3,1,4],0))

t3=("""hola mundo,
como estas.

ha pasado muncho,
desde ese dia.""").split("\n\n")      #separar por parrafos eliminando "\n"
#t3='\n\n'.join(t3)                   #unir por parrafos

def split_split_parrafos(t):          #separa [  ['hola','mundo'] , ['como',estas']  ]
    l=[]
    for k in t:
        l+=[k.split()]
        #l+=[book(k.split())]
    return l
#print(split_split_parrafos(t3))

#x=list("hola mundo como estas ")
#x[-1]=','
#x=''.join(x)
x="hola mundo como estas!"
x=x[:-1]+','                           #replace last element for ','
#x[-1]='.'                             #TipeError 'str' not support change

t4="""hola mundo,
como estas.

ha pasado muncho,
desde ese dia."""
def split_parrafos(t,separador):       #separar por parrafos sin eliminar "\n"
    l=[]
    texto=''
    for k in t:
        texto+=k
        if k==separador:
            l+=[texto]
            texto=''
    l+=[texto]
    return l
#print(split_parrafos(t4,"\n"))

#input:  hola mundo. como estas. de tiempo.  , [',', '?', '.']
#output: hola mundo, como estas? de tiempo.
def back_sign(t,l):
    m=t.split('\n\n')
    n=''
    for k in range(len(m)):
        t=m[k].split()
        x=0
        for k in range(len(t)):
            if (t[k][-1]=='.'):
                t[k]=t[k][:-1]+l[x]
                x+=1
        n+=' '.join(t)+'\n\n'
    return n



