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

def replace_ipa(t):
    t=t.replace("a","â")
    t=t.replace("e","ê")
    t=t.replace("o","ô")
    t=t.replace("i","î")
    t=t.replace("u","û")
    
    t=t.replace("p","pʰ")#ƥ
    t=t.replace("b","ɓ")
    t=t.replace("t","ʈ")
    t=t.replace("d","ɖ")
    t=t.replace("k","kʰ")#Ʞʞ
    t=t.replace("g","ɠ")
    t=t.replace("m","ɱ")
    t=t.replace("n","ɲ")
    
    t=t.replace("f","ʄ")
    t=t.replace("v","ⱱ")
    t=t.replace("s","ʂ")
    t=t.replace("z","ʐ")
    t=t.replace("h","ɦ")
    t=t.replace("l","ɭ")
    t=t.replace("j","ʝ")
    t=t.replace("r","ɹ")
    t=t.replace("y","ɣ")
    t=t.replace("w","ɰ")
    return t


def replace_letter(t1):
    t=t1.replace("ch","Ç")
    t=t.replace("h","")
    t=t.replace("H","")
    t=t.replace("; "," - ")
    t=t.replace(" ","_")
    t=t.replace("a","á")
    t=t.replace("e","é")
    t=t.replace("y ","í ")
    t=t.replace("i","í")
    t=t.replace("o","ó")    
    t=t.replace("u","ú")
    return t


t1=read_unicode("4000-5000.txt")
t_ipa=read_unicode("4000-5000 IPA.txt")
lines=t1.split("\n")
ipa=t_ipa.split("\n") 

def replace_spanish_letter(lines,ipa):
    for k in range(1,len(lines),2):###impares=spanish    
        lines[k]="["+replace_letter(lines[k])+"]"

    j=0
    for k in range(0,len(lines),2):###pares=ingles
        spelling=list(lines[k])
        lines[k]="["+lines[k]+"] ["+"_".join(spelling)+"] "+" ".join(list(replace_ipa(ipa[j])))
        j+=1
    
    return lines




lines=replace_spanish_letter(lines,ipa)
lines=[lines[par+1]+" "+lines[par]+"\n" for par in range(0,len(lines),2)]
#for x in lines: print(x) 
#for x in range (0,len(lines),2): print(lines[x])

lines="\n".join(lines)
lines=lines.replace("] [","]\n[")
lines=lines.replace("[ ","[")
lines=lines.replace("ˈ ","ˈ")
lines=lines.replace("ˌ ","ˌ")
lines=lines.replace(" ʰ","ʰ")

write_unicode(lines,"4000-5000 IPA merger.txt")





























