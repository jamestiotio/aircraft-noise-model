# Draw violin plot for night sleep hours
# Created by James Raphael Tiovalen (2019)

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("responses.csv")
ax = sns.violinplot(x="Uni", y="Sleep", data=df, inner="quartile")
ax.set(xlabel="Public University", ylabel="Amount of Night Sleep (hours)")
ax.set_title("Plot of Amount of Night Sleep against Public University\n")
plt.show()
