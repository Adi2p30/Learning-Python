discounts = 0
print('Welcome to the harry potter bookstore\n'
      'each book costs 8 Eur')
books = [0,0,0,0,0]
discount = [0,5,10,15,20,25]
booklst = []
distbooklst = []
Numbooks = int(input('How many Books do you wish to buy? '))
for i in range(0,Numbooks):
    Book = int(input('Which Book do you wish to buy? '))
    booklst.append(Book)
    for j in range(0,len(booklst)):
        print("You bought book number " + str(booklst[j]) , end= "\n")
    for book in booklst:
        if book not in distbooklst:
            distbooklst.append(book)
            discounts = discounts+1
totalprice = (Numbooks*8) - ((Numbooks*8)*((discount[discounts])/100))
print(totalprice)


