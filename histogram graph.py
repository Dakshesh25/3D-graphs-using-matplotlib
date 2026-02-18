

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Class" : ["A","A","B","B","C","C"],
    "Subject": ["math","science","math","science","math","science"],
    "Marks": [80,70,85,75,60,80]
}
df = pd.DataFrame(data)
sns.set_theme(style = 'whitegrid', palette = "vlag")
sns.barplot(x = "Class",y = "Marks" , hue = "Subject", data = df)

plt.show()
