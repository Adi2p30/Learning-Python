def emotionmodel1(person):
    from Inputtaker import situations
    print(situations.keys())
    person = input("which person?: ")
    persondata = situations[person]
    Happylst = []
    Angrylst = []
    Surpriselst = []
    Sadlst = []
    Fearlst = []
    numberlst = []
    allpatterns = []
    for i in range(0, len(situations[person]["5emotions"])):
        Happylst.append(situations[person]['5emotions'][i]['Happy'])
        Angrylst.append(situations[person]['5emotions'][i]['Angry'])
        Surpriselst.append(situations[person]['5emotions'][i]['Surprise'])
        Sadlst.append(situations[person]['5emotions'][i]['Sad'])
        Fearlst.append(situations[person]['5emotions'][i]['Fear'])
        numberlst.append(i)
    emotioni = input("which emotion? (Happy, Angry, Surprise, Sad, Fear)")
    for i in range(0, len(situations[person]["5emotions"])-1):

