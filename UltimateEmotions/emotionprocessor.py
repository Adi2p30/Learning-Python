
import text2emotion as te
def Emotiontracker():
    ego = 0
    from Inputtaker import situations
    print(situations.keys())
    person = input("which person?: ")
    persondata = situations[person]
    def emotionappender():
        for i in range(0,len(situations[person]['messeges'])):
            situations[person]['5emotions'].append(te.get_emotion(situations[person]['messeges'][i]))
    def egoformula():
        for i in range(0,len(situations[person]["5emotions"])):
            ego = ego + 1.3*(situations[person]["5emotions"][i]['Happy']) + -0.5*(situations[person]["5emotions"][i]['Fear']) + 1.2*(situations[person]["5emotions"][i]['Angry'])
        ego = ego/2
    def politeness():
        print("cool")
    emotionappender()
    egoformula()
def wordprocessing():
    from Inputtaker import situations
    print(situations.keys())
    person = input("which person?: ")
    for i in range(0,len((situations[person]['messeges']))):
        text = (situations[person]['messeges'][i])
        text = text.split(" ")
        for j in range(0,len(text)):
            if text[i] in (situations[person]["processedmesseges"]):
                (situations[person]["processedmesseges"][text[j]]) = (situations[person]["processedmesseges"][text[j]]) + 1
            else:
                situations[person]["processedmesseges"].append
print(te.get_emotion("proo"))