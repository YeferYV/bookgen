def read_unicode(t1):
    file = open(t1, "r", encoding="utf-8")
    return file.read()
    file.close()

def write_unicode(t1,title):
    file = open(title, "w", encoding="utf-8")
    return file.write(t1)
    file.close()

#out1 ="(嘉南大圳 ㄐㄧㄚ　ㄋㄢˊ　ㄉㄚˋ　ㄗㄨㄣˋ )"
#write_unicode(out1)
#text1=read_unicode("new_text.txt")
#print(text1)

parrafo =lambda texto   : texto.split("\n\n")
line    =lambda parrafo : [parrafo[k].split("\n") for k in range(len(parrafo))]
word    =lambda line    : [   [line[j][i].split() for i in range(len(line[j]))]   for j in range(len(line))]
#print(word(line(parrafo(t))))

#j_texto   =word(line(parrafo(t)))
j_parrafo =lambda texto   : "\n\n".join(texto)
j_line    =lambda parrafo : ["\n".join(parrafo[k]) for k in range(len(parrafo))]
j_word    =lambda line    : [[" ".join(line[j][i]) for i in range(len(line[j]))]   for j in range(len(line))]
#print(j_parrafo(j_line(j_word(j_texto))))

t1="""primera linea, first line,
segunda linea. second line.

cuarta linea, fourth line,
quinta linea. fifth line."""

t2="""first line,
second line.

fourth linea,
fifth linea."""

def replace_apostrophe(t1):
    t=t1.replace("n't"," not")
    t=t.replace("'m"," am")
    t=t.replace("'re"," are")
    t=t.replace("'ll"," will")
    t=t.replace("'d"," had")
    t=t.replace("'ve"," have")
    return t

def replace_letter(t1):
    t=t1.replace("ch","ÇH")
    t=t.replace("h","")
    t=t.replace("H","")
    #t=t.replace("ja","JÂ")
    #t=t.replace("je","JÊ")
    #t=t.replace("ji","JÎ")
    #t=t.replace("jo","JÔ")
    #t=t.replace("ju","JÛ")
    #t=t.replace("ge","GÊ")
    #t=t.replace("gi","GÎ")
    #t=t.replace("qu","k")
    #t=t.replace("Qu","k")
    t=t.replace(" ","_")
    t=t.replace("a","á")
    t=t.replace("e","é")
    t=t.replace("y ","í ")
    t=t.replace("i","í")
    t=t.replace("o","ó")
    t=t.replace("u","ú")
    return t
#print(replace_letter(t1))

import string                                           #sign: ◄ ■ ► ● ♦ ▲▼
def change_sign_(text):                                #input: ['primera linea, first line,\nsegunda linea. second line.\n\ncuarta linea, fourth line,\nquinta linea. fifth line.']
    text=text.replace('...','... ')
    text=text.replace('*','')
    text=text.replace('(','')
    text=text.replace(')','')
    text=text.replace('"','')
    text=text.replace('”','')
    text=text.replace('“','')
    text=text.replace('\n\n',' ')
    text=text.replace('\n',' ')
    text=text.replace('- ','. ')
    text=text.replace('?','?.')
    bypass=["'",'-','_','?']
    for char in text:
        if (char not in bypass) and (char in string.punctuation):
                text=text.replace(char,"\n►")
    text=text.replace('►\n','')
    beginning=['►'+x for x in string.ascii_letters]+['►'+str(y) for y in range(10)]+["►'"]
    for char in beginning:
        text=text.replace(char,char[0]+' '+char[1])
    text=text.replace('► \n','')
    return ["► "+text[:-2]]
#print(change_sign_(t1))

#input:   'primera linea,\nsegunda linea.\n\ncuarta linea,\nquinta linea.'
#output: ['primera linea ► \nsegunda linea ► \n\n\ncuarta linea ► \nquinta linea ► \n\n\n', [',', '.', ',', '.']]
def change_sign_2(text):
    text=text.replace('...','. ')
    text=text.replace('"','')
    text=text.replace('”','')
    text=text.replace('“','')
    bypass=["'",'-']
    text=word(line(parrafo(text)))
    new_text=''
    temp=''
    new_list=[]
    for _parrafo in text:
        for _line in _parrafo:
            for _word in _line:
                temp+=' '+_word
                for char in _word:
                    if (char not in bypass) and (char in string.punctuation):
                        new_list+=[char]
                        new_text+="►"+temp.replace(char,"\n")
                        temp=''
            #new_text+='\n'
        #new_text+='\n'
    return [new_text[:-1] , new_list]
t1_1=change_sign_2(t1)
t2_1=change_sign_2(t2)
#print(t1_1[0])

#input:   ['primera linea ► \nsegunda linea ► \n\n\ncuarta linea ► \nquinta linea ► \n\n\n', [',', '.', ',', '.']]
#output:   'primera linea,\nsegunda linea.\n\n\ncuarta linea,\nquinta linea.\n\n\n'
def back_sign_2(text):
    #new_text=text[0]
    for char in text[1]: text[0]=text[0].replace(" ► ",char,1)
    return text[0]
#print([back_sign_2(t1_1)])


#input:  ['primera linea ► \nsegunda linea ► \n\n\ncuarta linea ► \nquinta linea ► \n\n\n', [',', '.', ',', '.']]
#input:  ['first line ► \nsecond line ► \n\n\nfourth line ► \nfifth line ► \n\n\n'         , [',', '.', ',', '.']]
#input:  ['primera linea ► \nfirst line ► \nsegunda linea ► \nsecond line ► \n\ncuarta linea ► \n\nfourth line ►...
def linking_book(b1,b2):
    b1=b1.replace('\n','')
    b1=b1.split("►")
    b2=b2.replace('\n','')
    b2=b2.split("►")
    b3=''
    for k in range(len(b1)): b3+='\n►'+b1[k]+'.'+'\n►'+b2[k]+'.'
    return b3
#print(linking_book(t1_1[0],t2_1[0]))

def get_last_parrafo(t): return t.split('\n\n\n')[-1:]              #input: "first line \n\n\nlast line"          output:["last line"]
def get_parrafo(t,n): return '\n\n\n'.join(t.split('\n\n\n')[:n])   #input: "first line \n\n\nsecond line",1      output:"first line"
def number_parrafo(t): return len(t.split('\n\n\n'))                #input: hello world ► how are u ► long time ► output:3
def number_dots(t): return len(t.split("►"))                        #input: hello world ► how are u ► long time ► output:3
#number_dots = lambda  t:  len(t.split("◄►"))                       #input: hello world ► how are u ► long time ► output:3

################# TRANSFORMING BOOKS ####################
text="why i'm doing this"
#t3=read_unicode(text+".txt")
#t3=change_sign_(t3)
#write_unicode(t3[0],"► "+text+".txt")

t3=read_unicode("► "+text+".txt")
t4=read_unicode("► "+text+" translated.txt")
#print(number_parrafo(t3))
#t3=get_parrafo(t3,25)
#print(get_last_parrafo(t3))
#print("\n#################################")
#print("#################################\n")
#print(get_last_parrafo(t4))
#print(number_dots(t3),'\n',number_dots(t4))

t4=replace_letter(t4)
t5=linking_book(t4,t3)
write_unicode(t5,"► "+text+" spanish-english.txt")



