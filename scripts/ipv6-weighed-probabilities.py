import numpy as np
import pandas as pd
from utilities.plotting import plot_weighed_conditional_pairs

data1 = pd.read_csv('../data/raw/v6-conditional-probs-port-only-conditional.csv')
data1 = data1.sort_values('count_joint', ascending=False)
data1.head()

max_sample_size = data1['count_joint'].max()
max_sample_size
log_max_sample_size = np.log2(max_sample_size)
log_max_sample_size

# avg of top 3 sample size
log_avg_sample_size = np.log2(data1.head(3)['count_joint'].mean())
log_avg_sample_size

# weigh by log of their size and normalize
data1['prob_weighed'] = data1['probability']* np.log2(data1['count_joint']) / log_avg_sample_size
data1.head()

# plot both together in order of probabilites
# sort first
data1 = data1.sort_values('count_joint', ascending=False)
x1 = np.arange(len(data1))

plot_weighed_conditional_pairs(data1, ['port_b'], top_n=772, title = "IPv6 Weighed Conditional Probability P(port a | port b)", sav_location="../figures/figure-2b-ipv6-weighed-probabilities")