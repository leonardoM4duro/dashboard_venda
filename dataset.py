import json
import pandas as pd

file = open('dados/vendas.json', 'r')
data = json.load(file)

df = pd.DataFrame.from_dict(data)

print(df[:10])

file.close()