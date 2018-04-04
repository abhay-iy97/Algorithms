import itertools
def distinct(l):
    output=[]
    flat_list = [item for sublist in l for item in sublist]
    for i in flat_list:
            if i not in output:
                output.append(i)
    dict={}
    for j in output:
        dict[j]=flat_list.count(j)
    print(dict)
    return dict

def count(m,l):
    c=0
    dict={}
    pos=1
    for x in m:
        for item in l:
            for i in range(0,len(x)):
                if x[i] not in item:
                    pos=0
                    break
            if(pos!=0):
                c+=1
            pos=1
        dict[x]=c
        c=0
    return dict

def prune(dict,min_support):
    new_dictionary={}
    for k in dict.keys():
        if (dict[k] >= min_support):
            new_dictionary[k] = dict[k]
    return new_dictionary

def listCreation(d):
    l=[]
    for k in d.keys():
        l.append(k)
    return l

file=open("C:\\Users\\MAHE\\Desktop\\test_apriori.csv","r")
l=[]
min_support=int(input("Enter min support: "))
while(True):
    line=file.readline().strip()
    if(line==''):
        break
    l.append(line.split(','))
dict=distinct(l)
new_dict={}
new_dict=prune(dict,min_support)
print("Level 1")
print(new_dict)
max_dict={}
x=[]
i=2
while(True):
    for subset in itertools.combinations(listCreation(new_dict),i):
        x.append(subset)
    max_dict=count(x,l)
    max_dict=prune(max_dict,min_support)
    print("Level: "+str(i))
    print(max_dict)
    x = []
    if(len(max_dict.keys())==0):
        break
    i += 1
