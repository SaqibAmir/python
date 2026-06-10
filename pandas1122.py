import pandas as pd
import numpy as np
# my_file = pd.DataFrame(
#     [[1, 20, 35, 4], [2, 5, 6, 7], [8, 9, 76, 9]],
#     ['row1', 'row2', 'row3'],
#     ['col1', 'col2', 'col3', 'col4']
# )
# print(my_file)
# print(my_file.describe())
d = pd.DataFrame(
    np.arange(1, 51).reshape(10, 5),
    index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6', 'row7', 'row8', 'row9', 'row10'],
    columns=['col1', 'col2', 'col3', 'col4', 'col5']
)

print(d)
print(d.describe())
c={
    "person1":{"name":"saqib","salary":2500,"format":"YD"},
    "person2":{"name":"haseeb","salary":3008,"format":"RD"},
    "person3":{"name":"muneeb","salary":78763,"format":"ZD"}

}
m=pd.DataFrame(c)
print(m)
print(m.head(2))
print(m.tail(2))
print(m["person1"],["person2"])

print(m.loc["salary"])
m.to_csv("my file.csv")

f=pd.read_csv("my file.csv")
print(f)
print(f.describe())
