import pandas as pd

data = pd.read_csv('covid_file.csv')

certain_column = data.iloc[:,6:7].values.tolist()

count = 0
for i in certain_column:
    print(i[0])
    if i[0] == '70+':
        count+=1;
print('70+ -> {}'.format(count))
print(len(certain_column))
