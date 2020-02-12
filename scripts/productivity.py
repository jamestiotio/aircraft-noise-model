# Draw violin plot for productivity hours
# Created by James Raphael Tiovalen (2019)

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("responses.csv")
ax = sns.violinplot(x="Uni", y="Productivity", data=df, inner="quartile")
ax.set(xlabel="Public University", ylabel="Productivity for Studies (hours)")
ax.set_title("Plot of Productivity for Studies against Public University\n")
plt.show()
