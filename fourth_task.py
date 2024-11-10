import pandas as pd

products = pd.read_csv('./58/fourth_task.txt')
products = products.drop("production_date", axis=1)
mean_quantity = products.quantity.mean()
max_rating = products.rating.max()
min_quantity = products.quantity.min()
filtered = products[products.status != 'New']

filtered.to_csv("./results/fourth_task.csv")
with open('./results/fourth_task.txt', 'w+') as file:
    file.write(f"{mean_quantity}\n")
    file.write(f"{max_rating}\n")
    file.write(f"{min_quantity}\n")