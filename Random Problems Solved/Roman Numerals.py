inpnumber = input('Choose a Roman Numeral ')
romannumbers = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}
def romantoint(inpnumber):

    inputlist = list(inpnumber)
    romanInt = 0
    prevNumber = 0
    for num in inputlist:

        if romannumbers.__contains__(num):
            currentNumber = romannumbers[num]
            if(prevNumber < currentNumber):
                if currentNumber != 'I':
                    romanInt += currentNumber - (prevNumber * 2)

            else:
                romanInt += romannumbers[num]
            prevNumber = romannumbers[num]
    return romanInt

while inpnumber != 'Exit':
    inpnumber = input('Choose a Roman Numeral ')
    output = romantoint(inpnumber)
    print(output)