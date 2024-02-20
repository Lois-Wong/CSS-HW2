import pandas as pd
import random
original = pd.read_csv('data/common2.csv')
new = pd.DataFrame(columns = ['comment'])
random.seed(12)
repeats = []
for i in range(40):
    exact = original.sample(2, replace=False)
    text = f"Response 1: {exact['comment'].values[0]} \n Response 2: {exact['comment'].values[1]}"
    if text in repeats:
        i = i-1
    else:
        new.loc[len(new.index)] = [text]
        repeats.append(text)
new.to_csv('new_common2.csv', index=True)

