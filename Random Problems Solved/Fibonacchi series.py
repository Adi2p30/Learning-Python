serieslst = [0,1,1,2,]
for i in range(4,100000):
    serieslst.append((serieslst[i-1]) + (serieslst[i-2]))
inpnumber = int(input('Which number? '))
if inpnumber in serieslst:
    print('Yes ' + str(inpnumber) + ' is in the fibonacchi series')
else:
    print('No ' + str(inpnumber) + " isnt in the fibanochi series")