import matplotlib.pyplot as plt
runsin1 = [10,23,9,76,20,290,12,2,3,74,11,0,27,0]
runsin2 = ["na",51,0,50,"na","na",19,14,4,72,62,"na","na"]
Pitchtype = [8,6,7,6,9,6,8,9,7,4,5,10,10]
numberlst = []
preflst = []
def runs():
    plt.xlabel('runs')
    plt.ylabel('testmatch')
def overall():
    for i in range(0,13):
        if runsin2[i] != 'na' and runsin1[i] != 'na':
            preformance = 10*runsin1[i] + 10*runsin2[i]+ 3*Pitchtype[i]
            numberlst.append(i)

        elif runsin2[i] == "na":
            preformance = 20 * runsin1[i] + 3 * Pitchtype[i]
            numberlst.append(i)

        elif runsin1[i] == "na":
            preformance = 20 * runsin2[i] + 3 * Pitchtype[i]
            numberlst.append(i)
        preflst.append(preformance/1000)
    plt.plot(numberlst, preflst, label="Preformance", marker='o')
    plt.title('KOHLI SUKS')
    plt.legend()
    plt.show()
overall()
