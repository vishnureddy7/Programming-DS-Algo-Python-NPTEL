#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs08/progassignment?name=99

def isprime(n):
    if(n<=1):
        return False;
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False;
    return True;

def prime_generator(n):
    for i in range(2,n):
        if(isprime(i)):
            yield i;

def primepartition(n):
    #alternative version
    #if(n<=3):
    #    return False;
    #for i in range(1,n):
    #    if(isprime(i) and isprime(n-i)):
    #        return True;
    #return False;
    prime=prime_generator(n);
    while(True):
        try:
            i=next(prime);
        except Exception:
            return False;
        if(isprime(n-i)):
            return True;
    return False;

def nestingdepth(s):
    stack=[];
    maxi=0;
    depth=0;
    for i in s:
        if(i=='('):
            stack.append('(');
            depth+=1;
        elif(i==')'):
            try:
                stack.pop();
                depth-=1;
            except IndexError:
                return -1;
        if(maxi<depth):
            maxi=depth;
    if(stack==[]):
        return maxi;
    return -1;


def rotatelist(l,k):
    k=k%(len(l));
    return l[k:]+l[:k];

