sum1 = 0
sum2 = 0
for i in range(0,100):
    sum1 = sum1 + (i*i)
for i in range(0,100):
    sum2 = sum2 + i

print(str((sum2 * sum2)-sum1))