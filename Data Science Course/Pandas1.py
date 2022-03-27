import pandas as pd

marks = {

    'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya'],
    'Age': [21, 19, 20, 18, 17, 21],
    'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
    'Percentage': [88, 92, 95, 70, 65, 78]

        }

mark = pd.DataFrame(marks)
filtereddf1 = mark[mark["Percentage"] > 80]
print(filtereddf1)
print("\n")
filtereddf2 = mark.loc[mark["Percentage"] > 80]
print(filtereddf2)

