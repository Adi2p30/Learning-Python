a = [7, 2, 4, 9, 3, 8, 4, 1]
def sortAdi(a):
    b = []
    while a:
        smal = a[0]
        for x in a:
            if x < smal:
                smal = x
        b.append(smal)
        a.remove(smal)
    print(b)

def sort(a):

    for i in range(0,a.length):



sortAdi(a)