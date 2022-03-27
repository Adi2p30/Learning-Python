var = 0
num = 1
while var != 14:
    num = num + 1
    for i in range(11,15):
        if num%i == 0:
            var = var + 1
        else:
            var = 0
print(num)