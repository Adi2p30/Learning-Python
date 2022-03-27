flag = ""
commonsigndict = {}
signslst1 = []
cursigns = []
commonsigns = []
currlinedata = []
signslst2 = []
correctmeter = 0
file1 = open('Data.txt', 'r')
lines = file1.readlines()
for i, line in enumerate(lines):
    currlinedata = (lines[i].split(" "))
    currlinedata[1] = currlinedata[1].replace("\n","")
    signs = currlinedata[0]
    result = currlinedata[1]
    if result == '1':
        for i in range(0, len(signs), 2):
            signslst1.append(signs[i:i+2])
            cursigns.append(signs[i:i + 2])
        for i in range(1, len(signs), 2):
            signslst1.append(signs[i:i+2])
            cursigns.append(signs[i:i + 2])
        for r in range(0, len(cursigns)):
            if cursigns[r] in signslst1:
                commonsigns.append(cursigns[r])
                if cursigns[r] in commonsigndict.keys() and cursigns[r] not in signslst2:
                    commonsigndict[cursigns[r]] = commonsigndict[cursigns[r]] + 1
                else:
                    commonsigndict[cursigns[r]] = 1
                if cursigns[r] not in signslst2:
                    correctmeter = correctmeter + 1
    else:
        for i in range(0, len(signs), 2):
            signslst2.append(signs[i:i+2])
            cursigns.append(signs[i:i + 2])
        for i in range(1, len(signs), 2):
            signslst2.append(signs[i:i+2])
            cursigns.append(signs[i:i + 2])
    cursigns = []
    if correctmeter >= 6:
        flag = 'PATTERNachieved'
print(commonsigndict)
print("The pattern is "+max(commonsigndict, key=commonsigndict.get))