'''
n=input()

def findsize(l):
    se=set(l)
    return len(se)
l=[]
size=0
for i in range(len(n)):
    l.append(n[i])
    siz=findsize(l)
    if(size<siz):
        size=siz
    #print("Among all substring of length",i+1,",maximum of distinct characters =",siz)
print(size)
'''
def maxchar(st,n):
    count=[0]*256
    for i in range(n):
        count[ord(st[i])]+=1
    maxdist=0
    for i in range(256):
        if(count[i]!=0):
            maxdist+=1

    return maxdist
def smallsub(st):
    n=len(st)
    maxdist=maxchar(st,n)
    minl=n
    for i in range(n):
        for j in range(n):
            sub=st[i:j]
            sub_dist=maxchar(st[i:j],len(sub))
            if(len(sub) < minl and maxdist == sub_dist):
                minl=len(sub)
    return minl

n=input() 
l=smallsub(n)
print(l)
               
    
