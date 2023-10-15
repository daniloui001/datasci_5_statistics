import pandas as pd
from faker import Faker
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

df = pd.read_csv('https://raw.githubusercontent.com/daniloui001/datasci_5_statistics/main/ER%20visits%20vs.%20Bene.csv')

### Alocohol abuse = higher ER visits// 17 = Alcohol Abuse/24 = Alzehimer's Disease,Dementia/32 = Arthritis/92 = Asthma

chi2, p, dof, expected = chi2_contingency(df[['ER_Visits_Per_1000_Benes', 'Bene_Cond']])

print(f"Chi-Square Statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies: ")
print(expected)

alpha = 0.05  # Significance level
if p < alpha:
    print("There is a significant association between the categories.")
else:
    print("There is no significant association between the categories.")