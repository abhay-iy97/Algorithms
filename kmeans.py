import numpy
def calcDist(a,m):
       dist=[]
       i=0
       for key, value in a.items():
              point1=numpy.array((key[0],key[1]))
              dist.append(numpy.linalg.norm(point1 - m))
              i+=1
       return dist

def getKey(a,i):
       j=0
       for key,values in a.items():
              if(j==i):
                     return key
              j+=1

def AssignCluster(distances,a):
       min=10000
       pos=-1
       for i in range(0,n):
              for j in range(0,k):
                     if(distances[j][i]<min):
                            min=distances[j][i]
                            pos=j
              min=10000
              a[getKey(a,i)]=pos
       print(a)

def Centroid(a):
       x=[]
       y=[]
       z={}
       for i in range(0,k):
              for key,items in a.items():
                     if(items==i):
                            x.append(key[0])
                            y.append(key[1])

              new_x = float(sum(x, 0) / len(x))
              new_y = float(sum(y, 0) / len(y))
              x=[]
              y=[]
              z[i]=(new_x,new_y)
       return z

k= int(input("Enter k"))
n= int(input("Enter n"))
a={}
for i in range (0,n):
       x=float(input("Enter x "))
       y=float(input("Enter y "))
       a[(x,y)]=-1
temp=k
distances=[]
for key,value in a.items():
       if(temp==0):
              break
       point2=numpy.array((key[0],key[1]))
       distances.append(calcDist(a,point2))
       temp-=1

AssignCluster(distances,a)
z=Centroid(a)
print(z)
dist=[]
for i in range(0,5):
       for key,items in z.items():
              send=numpy.array((items[0],items[1]))
              dist.append(calcDist(a,send))
       AssignCluster(dist,a)
       z=Centroid(a)
       dist=[]

print(a)