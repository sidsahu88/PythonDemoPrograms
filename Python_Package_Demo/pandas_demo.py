import pandas as pd


csv_file = "ML_Demo\music.csv"  # csv file is present at parent directory of this program.
df = pd.read_csv(csv_file)  # df is dataframe holding data present in file

print(df.head())
print('\n')
print(df['genre'])
print('\n')
print(df[['genre']])
print('\n')
print(df[['age', 'gender']])
print('\n')
print(df.iloc[2:3, 0:3])
print('\n')
print(df.iloc[5, 2])
print('\n')
print(df.loc[8, 'genre'])
print('\n')
print(df[df['genre'] == 'Classical'])  # Get all the dataframe where genre is classical only
