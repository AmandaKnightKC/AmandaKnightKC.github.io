# Import libraries:
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt

# Define the data frame:
pairs = [[34, 5], [108, 17], [64, 11], [88, 8], [99, 14], [51, 5]]
df = pd.DataFrame(pairs, columns=['bill', 'tip'])

# Perform visual linear regression analysis with Seaborn:
sns.set(color_codes=True)
sns.regplot(x='bill', y='tip', data=df, label='tips')
sns.residplot(x='bill', y='tip', data=df, label='residuals')

# Display the result with Matplotlib:
plt.legend()
plt.show()