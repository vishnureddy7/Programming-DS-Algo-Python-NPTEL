#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs08/progassignment?name=102

def progression(l):
  i,j=0,1;
  n=len(l);
  if(n<=1):
    return True; 
  d=l[0]-l[1];
  while(j<n):
    if(l[i]-l[j]!=d):
      return False; 
    i,j=i+1,j+1;
  return True;

def primesquare(l):
    n=len(l);
    if(n<=1):
        return True;
    return square_prime(l,0) or square_prime(l,1);

#wrong submission :(
'''def square_prime(l,rem):
    start=l[rem];
    n=len(l);
    for i in range(n):
        if(i%2==rem):
            if(l[i]!=start**(i//2+1)):
                return False;
        else:
            if(not isprime(l[i])):
                return False;
    return True;
'''

def square_prime(l,rem):
  n=len(l);
  for i in range(n):
    if(i%2==rem):
      if(not issquare(l[i])):
        return False;
    else:
      if(not isprime(l[i])):
        return False;
  return True;

def issquare(n):
  return int(n**0.5)**2==n;

def isprime(n):
    if(n<=1):
        return False;
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False;
    return True;

def matrixflip(m,d):
    m=m[:]
    if(d=='h'):
        n=len(m);
        for i in range(n):
            m[i]=m[i][-1::-1];
    elif(d=='v'):
        m=m[-1::-1];
    return m;
