#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs08/progassignment?name=98

def intreverse(n):
    #alternative version
    #r=0;
    #while(n!=0):
    #   (r,n)=(r*10+n%10,n//10);
    return int(str(n)[-1::-1]);

def matched(s):
    stack=[];
    for i in s:
        if(i=='('):
            stack.append('(');
        elif(i==')'):
            try:
                stack.pop();
            except IndexError:
                return False;
    if(stack==[]):
        return True;
    return False;

def sumprimes(l):
    sum=0;
    for i in l:
        if(isprime(i)):
            sum=sum+i;
    return sum;

def isprime(n):
    if(n<=1):
        return False;
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False;
    return True;
