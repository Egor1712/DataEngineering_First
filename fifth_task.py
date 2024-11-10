import pandas as pd

data = pd.read_html("./58/fifth_task.html", encoding='utf8')[0]
data.to_csv('./results/fifth_task.csv')