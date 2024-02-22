import pandas as pd

data = [
    ["Orange", "orange", "bumpy", 150, "tangy", "yes"],
    ["Banana", "yellow", "smooth", 127, "sweet", "no"],
    ["Kiwi", "brown", "spikes", 111, "tart", "yes"],
    ["Apple", "red", "smooth", 137, "sweet", "yes"],
    ["Pineapple", "yellow", "spikes", 166, "tangy", "no"],
    ["Cherry", "red", "smooth", 83, "tart", "yes"],
    ["Strawberry", "red", "bumpy", 95, "tart", "yes"],
    ["Grape", "purple", "smooth", 110, "tart", "yes"],
    ["Blue-Berry", "blue", "smooth", 78, "tart", "yes"],
    ["Mango", "green", "rough", 154, "tart", "yes"],
    ["Orange", "orange", "bumpy", 142, "tangy", "yes"],
    ["Banana", "yellow", "smooth", 121, "sweet", "no"],
    ["Kiwi", "brown", "spikes", 117, "tart", "yes"],
    ["Apple", "red", "smooth", 136, "sweet", "yes"],
    ["Pineapple", "yellow", "spikes", 167, "tangy", "no"],
    ["Cherry", "red", "smooth", 85, "tart", "yes"],
    ["Strawberry", "red", "bumpy", 92, "tart", "yes"],
    ["Grape", "purple", "smooth", 108, "tart", "yes"],
    ["Blue-Berry", "blue", "smooth", 75, "tart", "yes"],
    ["Mango", "green", "smooth", 157, "tart", "yes"],
    ["Orange", "orange", "bumpy", 149, "tangy", "yes"],
    ["Banana", "yellow", "smooth", 123, "sweet", "no"],
    ["Kiwi", "brown", "spikes", 114, "tart", "yes"],
    ["Apple", "red", "smooth", 133, "sweet", "yes"],
    ["Pineapple", "yellow", "spikes", 162, "tangy", "no"],
    ["Cherry", "red", "smooth", 84, "tart", "yes"],
    ["Strawberry", "red", "bumpy", 98, "tart", "yes"],
    ["Grape", "purple", "smooth", 101, "tart", "yes"],
    ["Blue-Berry", "blue", "smooth", 76, "tart", "yes"],
    ["Mango", "green", "smooth", 156, "tart", "yes"]
]

df = pd.DataFrame(data,
                  columns=["Fruit_name", "Fruit_color", "Fruit_texture", "Fruit_size", "Fruit_taste", "Seed/Seed_less"])

with pd.ExcelWriter('Fruit_dataset.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
