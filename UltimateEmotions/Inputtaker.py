def inputa():
    text = input("")
inputa()

#___________
situations = {
    "Aditya": {
        "5emotions": [],
        "messeges":[],
        "processedmesseges":{},
        "para":"",
        "codesituations":[],
        "otheremotions":[],
        "specificsituation" : []
               },

    "Paary": {
        "5emotions": [],
        "messeges":[],
        "para":"",
        "processedmesseges":{},
        "otheremotions":[],
        "specificsituation" : []
               },
#otheremtions are of (ego, politeness, helpfullness, trust, Studious)
}
#_______

relationships = [],
friends = [],
shortcuts = {
    "wbu" : "what about you?",
    "u" : "you",
    "istg":"I s wear to god"
            }
def inputsit():
    name = input("whos directory?: \n")
    if name in situations.keys():
        situation = input("")