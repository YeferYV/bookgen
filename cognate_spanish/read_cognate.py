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


def replace_letter(t1):
    t=t1.replace("ch","Ç")
    t=t.replace("h","")
    t=t.replace("H","")
    t=t.replace(" ","_")
    t=t.replace("a","á")
    t=t.replace("e","é")
    t=t.replace("y ","í ")
    t=t.replace("i","í")
    t=t.replace("o","ó")    
    t=t.replace("u","ú")  
    return t


t1=read_unicode("spanish-english cognates.txt")
lines=t1.split("\n")
def replace_spanish_letter(lines):
    for k in range(len(lines)):
        lines[k]=lines[k].split("-")
        lines[k][0]=replace_letter(lines[k][0])
        lines[k]="-".join(lines[k])
    return lines

lines=replace_spanish_letter(lines)
#for x in lines: print(x)
lines="\n".join(lines)

write_unicode(lines,"cognates.txt")
















