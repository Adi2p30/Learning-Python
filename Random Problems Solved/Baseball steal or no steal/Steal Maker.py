import random
fg = open("Data.txt", "a")
pro = 0
string = ""
string2 = ""
prolly = 0
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pattern = random.choice(letters) + random.choice(letters)
print(pattern)
for j in range(1,random.randint(15, 30)):
    string = ""
    finalstring = ""
    string2 = ""
    prolly = random.randint(0, 1)
    for i in range(10,random.randint(20,50)):
        string = string + random.choice(letters)
    for i in range(10, random.randint(1, 10)):
        string2 = string2 + random.choice(letters)

    if prolly >= 1:
        finalstring = string + pattern + string2
        string = ""
        fg.write(str(finalstring) + " " + str(prolly) + "\n")
    elif prolly == 0:
        finalstring = string
        fg.write(str(finalstring) + " " + str(prolly) + "\n")
