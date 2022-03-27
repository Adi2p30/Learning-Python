sum =0
i = 3
serieslst = [0,1,1,2,]
for i in range(0,500):
    serieslst.append((serieslst[i-1]) + (serieslst[i-2]))
    if serieslst[i] %2 == 0:
        sum = sum + serieslst[i]
print("The sum of even numbers in the fibonacchi sequence untill 1000000 million is: " + str(sum))