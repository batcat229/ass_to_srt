import codecs

def read_between(context,a,b):
    start = 0      #Start position when searching
    end = 0        #End position of searching
    start = context.find(a)
    end = context.find(b)
    return context[start:end]

def clean(dialogue):
    t=dialogue
    start=t.find('{')
    end = t.find('}')
    while(start!=-1 & end!=-1):
        t=t[:start]+t[end+1:]
        start=t.find('{')
        end = t.find('}')
    return t

def gettime(line):
    part=line.split(',')
    time='0'+part[1]+' --> 0'+part[2]+'0'
    time=time.replace('.',',')
    return time

def getChinese(line):
    parts=line.split(',')
    text=parts[9]
    text=read_between(text,'','N')
    text=text[:-1]
    return text


file=codecs.open("33 Date Night 2 - w.srt","w",'utf-8')


a = codecs.open('33 Date Night 2 - w.ass','r','utf-8')
raw=a.read()
begin=raw.find('[Events]')
raw=raw[begin:]
dialogues = raw.split('Dialogue:') #get all the dialogues
for i in range(len(dialogues)):
    dialogues[i]=clean(dialogues[i])

row=4
n=1
while row < len(dialogues):
    line=dialogues[row]
    if(line.find('译者')==-1):
        time=gettime(line)
        text=getChinese(line)
        m=str(n)
        L=(m+'\n'+time+'\n'+text+'\n'+'\n')
        file.write(L)
        n=n+1
    row=row+1

a.close()

file.close()