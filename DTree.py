import math

def getClasses(d):
    output=[]
    for x in d:
        if x not in output:
            output.append(x)
    return output

def Entropy(d,n):
    output = []
    m={}
    ent=0
    total=0
    for x in d:
        if x not in output:
            output.append(x)
    for i in output:
        m[i]=d.count(i)
        total+=d.count(i)
    print(m)
    for i in output:
        weight=(m[i]/total)
        ent+=weight*(math.log(weight,2))
    ent*=-1
    print(ent)

def InfoGain(d1,d2,k):
    output=getClasses(d1)
    dict={}
    x=[]
    for i in output:
        for j in range(0,len(d1)):
            if(i==d1[j]):
                x.append(d2[j])
        dict[i]=x
        x=[]
    AllClasses=getClasses(d2)
    tot=0
    sum=0
    for i in dict:
        for j in AllClasses:
            Dj=dict[i].count(j)
            D=len(dict[i])
            if(Dj==0):
                continue
            weight=(Dj/D)*math.log((Dj/D),2)
            tot+=weight
            print(weight,tot)
        if(weight==0):
            continue
        tot*=D/k
        sum+=tot
        tot=0

    sum*=-1
    return sum



file=open("C:\\Users\\MAHE\\Desktop\\DTree.csv","r")
l=[]

while(True):
    line=file.readline().strip()
    if(line==''):
        break
    l.append(line.split(','))
d={}
m=0
for i in l[0]:
    temp=0
    x=[]
    for j in l:
        if(temp==0):
            temp=1
            continue
        x.append(j[m])
    d[i]=x
    m+=1
print(d)

Entropy(d['class'],len(d['class']))

InfoG={}
for key,values in d.items():
    InfoG[key]=InfoGain(values,d['class'],len(d['class']))

print(InfoG)
