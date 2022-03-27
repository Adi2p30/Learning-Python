var = 0
num = 1
primelst = []
var1 = 0
while len(primelst) != 4:
    num = num + 1
    for i in range(2,num):
        if num%i == 0:
        else:
            var1 = var1+1
        if var1 == num - 1:
            primelst.append(var1)
print(max(primelst))

