import matplotlib.pyplot as plt


def plotemotions():
    from Inputtaker import situations
    plt.xlabel('time')
    plt.ylabel('timing')
    print(situations.keys())
    person = input("which person?: ")
    persondata = situations[person]
    Happylst = []
    Angrylst = []
    Surpriselst = []
    Sadlst = []
    Fearlst = []
    numberlst = []
    for i in range(0, len(situations[person]["5emotions"])):
        Happylst.append(situations[person]['5emotions'][i]['Happy'])
        Angrylst.append(situations[person]['5emotions'][i]['Angry'])
        Surpriselst.append(situations[person]['5emotions'][i]['Surprise'])
        Sadlst.append(situations[person]['5emotions'][i]['Sad'])
        Fearlst.append(situations[person]['5emotions'][i]['Fear'])
        numberlst.append(i)
    plt.plot(numberlst, Happylst, label="Happy", marker='o')
    plt.plot(numberlst, Angrylst, label="Angry", marker='o')
    plt.plot(numberlst, Surpriselst, label="Surprise", marker='o')
    plt.plot(numberlst, Sadlst, label="Sad", marker='o')
    plt.plot(numberlst, Fearlst, label="Fear", marker='o')
    plt.title(person + "'s " + 'emotions')
    plt.legend()
    plt.show()


plotemotions()
