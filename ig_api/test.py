import pandas as pd

saved_df = pd.read_csv('./saved.csv')


pk = 3121318818092333052

j = 0
for i in range(0,10):
    j = j+1
    if pk in saved_df['post pk'].values:
        break
    
print(j)
