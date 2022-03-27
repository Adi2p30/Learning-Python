factorlst = []
primefactorlst = []
tempvar = 0
num = int(input('ur number '))
for i in range(1,num):
    if num % i == 0:
        factorlst.append(i)
for j in range(1,len(factorlst)):
    for i in range(1,len(factorlst)):
       if (factorlst[j] % i) == 0:
           tempvar += 1
           if tempvar == 1:
               primefactorlst.append(factorlst[j])
print(max(primefactorlst))