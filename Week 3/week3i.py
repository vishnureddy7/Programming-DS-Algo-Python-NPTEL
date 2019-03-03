#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs08/progassignment?name=101

def descending(l):
    i,j=0,1;
    n=len(l);
    while(j<n):
        if(l[i]<l[j]):
            return False;
        i,j=i+1,j+1;
    return True;

def valley(l):
    inc,dec=1,1
    i,j=0,1;
    n=len(l);
    flow='inc'
    while(j<n):
        if(l[i]>l[j] and flow=='inc'):
            inc=inc+1;
        elif(l[i]<l[j] and flow=='inc'):
            flow='dec';
            dec=dec+1;
        elif(l[i]<l[j] and flow=='dec'):
            dec=dec+1;
        else:
            return False;
        i,j=i+1,j+1;
    if(inc>=2 and dec>=2):
        return True;
    return False;

def transpose(m):
    #alternative version
    #import numpy as np
    #ar=np.array(m);
    #return [list(i) for i in ar.transpose()];
    s=[];
    n=len(m[0]);
    for i in range(n):
        s.append([j[i] for j in m]);
        #k=[];
        #for j in m:
        #    k.append(j[0]);
        #s.append(k);
    return s;
