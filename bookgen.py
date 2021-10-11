#######SPLIT FOR SIGNS ONE BOOK LINE################
#input:   hola mundo, como estas?
#output:  [['hola mundo, '], ['como estas?, ']]
def splitbookln(l):
    l=l.split()
    l2=[]
    x=''
    for palabra in l:
        x+=palabra+' '
        for letra in palabra:
            if (letra==',') or (letra=='.'):
                l2+=[[x]]
                x=''
            elif (letra=='?') or (letra=='!'):
                x=x[:-1]+', '                #aniade coma en vez del espacio dejado
                l2+=[[x]]
                x=''
    return l2
l=splitbookln('hola mundo, como estas? de tiempo.')
l2=splitbookln('hello! god, longtime.')
l3="".join(["".join(k) for k in l])          #output:   hola mundo, como estas?, de tiempo.

##########CONVERT LIST TO STRING####################
#input:   [['hola mundo, '], ['como estas?, ']]
#output:  'hola mundo, como estas?,'
def joinbookln(l):
    texto=''
    for k in l:
        texto+=k[0]                          ###texto+=''.join(k)
    return texto
####print(joinbookln(l))

#######LINK SPANISH, ENGLISH, SPANISH##############################################
#input:   ([['hola mundo, '], ['como estas?, ']]    ,    [['hello!'],['god,']])
#output:  'hola mundo, hello!, como estas?, god,'
def linkbookln(l,l2):
    texto=''
    for k in range(len(l)):                  #MODIFICAR SI HAY FUERA DE RANGO
        texto+=l[k][0] + l2[k][0]
    return texto
#print(linkbookln(t,t2))

###############################################################################################################################
#####################################LONGLONGLONGLONGLONGLONGLONGLONGLONGLONG##################################################
###############################################################################################################################

##########SPLIT FOR PARAGRAPHS ONE BOOK#######
#input:   hola mundo,
#         como estas?
#output:  [[['hola mundo, ']], [['como estas?, ']]]
def splitbookln_long(t):
    t=t.split('\n\n')
    l=[]
    for parrafo in t:
        l+=[splitbookln(parrafo)]
        #t[parrafo]=splitbookln(t[parrafo])            #range(len(t)) return t   ###otra forma de resolver
        #print([splitbookln(parrafo)],'\n\n')
        #print("separaciones por parrafo    ",len(splitbookln(parrafo)))
    return t

b="""Alice was beginning to get very tired of sitting| by her sister on the bank|
and of having nothing to do|

Once or twice she had peeped into the book her sister was reading|
but it had no pictures or conversations in it|"""

b2="""Alice estaba empezando a cansarse de estar sentada| junto a su hermana en la orilla|
y de no tener nada que hacer|

Una o dos veces había mirado el libro que su hermana estaba leyendo|
pero no tenía fotos ni conversaciones|"""

b3=splitbookln_long("""Alice estaba empezando a cansarse de estar sentada, junto a su hermana en la orilla,
y de no tener nada que hacer.

Una o dos veces había mirado el libro que su hermana estaba leyendo,
pero no tenía fotos ni conversaciones.""")

b4="".join(["".join(["".join(j) for j in k])+'\n\n' for k in b])

#t=input("""""").split()                       #lee un parrafo
def leer(texto):                               #lee parrafos "txt"
    archivo1=open(texto,"r")
    return archivo1.read()
    archivo1.close()

t=splitbookln_long(leer("alice in the wonderful.txt"))
t2=splitbookln_long(leer("alicia en el pais de las maravillas.txt"))
t3=leer("alice.txt")
t4=leer("alicia.txt")
t5=leer("alice in the wonderful.txt")
t6=leer("alicia en el pais de las maravillas.txt")

##########CONVERT LIST TO STRING##########
#input:   [[['hola mundo, ']],[['como estas?, ']]]
#output:  hola mundo,
#         como estas?,'
def joinbookln_long(b):
    texto=''
    for k in range(len(b)):
        for j in range(len(b[k])):
            texto+=b[k][j][0]                    #texto+="".join(b[k][j])
        texto+='\n\n'
    return texto
#print(joinbookln_long(b2))

def joinbookln_long_modular(b):
    for k in range(len(b)):
        b[k]=joinbookln(b[k])
    return '\n\n'.join(b)
#print(joinbookln_long_modular(b2))

def linkbookln_long(b,b2):                       #output: english, spanish, english, spanish,...
    texto=''
    for k in range(len(b)):                      #MODIFICAR SI HAY FUERA DE RANGO
        for j in range(len(b[k])):
            #texto+=b[k][j][0] + b2[k][j][0]     #enlaza por comas english, spanish
            texto+=b[k][j][0]                    #enlaza todo el libro en ingles
        texto+='\n\n'
        for i in range(len(b[k])):
            texto+=b2[k][i][0]                   #enlaza todo el libro en espaniol

        texto+='\n\n\n\n\n'
    return texto
#print(linkbookln_long(t,t2))

def linkbookln_long_modular(b,b2):
    for k in range(len(b)):
        b[k]=linkbookln(b[k],b2[k])
    return '\n\n'.join(b)
#print(linkbookln_long_modular(b,b2))

###############################################################################################################
####################################### READ BOOK SIMPLIFIED ##################################################
###############################################################################################################

#input:  hola mundo, como estas? de tiempo.
#output: hola mundo| como estas| de tiempo|    ,    [',', '?', '.']
import string
def change_sign(t):
    t=t.split()
    l=[]
    for k in range(len(t)):
        for char in t[k]:
            if char in string.punctuation:
                l+=[char]
                t[k]=t[k].replace(char," ►",1)
    return ' '.join(t) , l
#print(change_sign('hola mundo, como estas? de tiempo.'))

def change_sign_long_modular(t):
    t=t.split('\n\n')
    l=[]
    for k in range(len(t)):
        t[k],l1=change_sign(t[k])
        l+=l1
    return [' '.join(t),l]
x=change_sign_long_modular(t3)
print(x)

#input:  hola mundo| como estas| de tiempo|      ,     [',', '?', '.']
#output: hola mundo, como estas? de tiempo.
def back_sign(t,l):
    t=t.split()
    x=0
    t2=''
    for k in range(len(t)):
        for char in t[k]:
            if char == "|":
                t[k]=t[k].replace(char,l[x],1)
                x+=1
    return ' '.join(t)
#print(back_sign('hola mundo. como estas. de tiempo.', [',', '?', '.']))

def back_sign_long_modular(x):
    t=x[0]
    l=x[1]
    t=t.split('\n\n')
    s=""
    for k in range(len(t)):
        s+=back_sign(t[k],l)
        #print(back_sign(t[k],l[k]))
    return s                                  #'\n\n'.join(t)
#print(   back_sign_long_modular( x )   )

#input: hello world| how are u| long time|        ,     [',' , '?' , '.']
#input: hola mundo| como estas| de tiempo|        ,     [',' , '?' , '.']
#output: hello world, hola mundo, how are u? como estas? long time. de tiempo.
def linkingbook(b,b2):
    b=b.replace('\n\n',' ')
    b=b.replace('\n',' ')
    b=b.split("|")
    b2=b2.replace('\n\n',' ')
    b2=b2.replace('\n',' ')
    b2=b2.split("|")
    #print((b),'\n\n',(b2),'\n\n')
    b3=''
    for k in range(len(b)):
        #print(b[k],b2[k])
        b3+=b2[k]+' |. \n'+b[k]+' |. \n'
    return b3
#print(linkingbook(x[0],t4))

#input: hello world| how are u| long time|
#output: 3
def NroDots(t):
    return len(t.split("►"))

#print(NroDots(x[0]),NroDots(t4))
#print(NroDots(t5),NroDots(t6))
#print(t5)
#l5=[2,5,10,15,20]
#s=lambda a,b: a+b
#x=lambda l: for a in l; l[a]
#print(s(1,2,3,4,5))
#l6=[0]
#l6=[l5[a] for a in range(0,len(l5))]
#l6=0
#l6+="".join(l5)
#print(l6)



