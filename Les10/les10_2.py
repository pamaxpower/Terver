"""
"""
from statsmodels.stats.multicomp import pairwase_tukeyhsd
import pandas as pd
import numpy as np

df = pd.DataFrame({'score': [70, 50, 65, 60, 75, 67, 74,
                             80, 74, 90, 70, 75, 65, 85,
                             148, 142, 140, 150, 160, 170, 155],
                    'group': np.repeat(['acountant', 'lawyer', 'programmer'], repeats=7)})

print(df)

tukey = pairwise_tukeyhsd(endog=df['score'],
                          groups=df['group'],
                          alpha = 0.05)

print(tukey)