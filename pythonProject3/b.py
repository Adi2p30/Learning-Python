t=int(input())
for i in range (0,t):
   k = int(input())
   m = int(input())
   n = int(input())
   print(k,m,n)
   if(m%(k*n))!=0:
      s=m//(k*n)
      r=m%(k*n)
      if(r%2==0):
         s=s+r//2
      else:
         s=s+1
         r=r-1
         s=s+r//2
   else:
      s=m/(k*n)
   print(s)