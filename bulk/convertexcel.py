import pandas as pd
import json
file = open("newns.json", "w")

holder = pd.read_excel("newns.xlsx", index_col=0)
output = holder.to_json()

file.write(output)
print("done")
