import pandas as pd
import matplotlib.pyplot as plt
import math as m

# df = pd.read_csv('data.csv')
#
# df["sqrt(y)"] = df["y_original"] ** (1/2)
#
# print(df)
#
# df1 = pd.read_csv('visualization.csv')
#
# plt.plot(df1["NOC"].value_counts())
# plt.show()

list = [-1,-0.5,0,0.5,1]
list1 = {}

def functionfx(x):
    value = 1 + m.exp(-x)
    return value

for a in list:
    v = a
    r = round(functionfx(a),2)

    list1.update({v:r})

print(list1)