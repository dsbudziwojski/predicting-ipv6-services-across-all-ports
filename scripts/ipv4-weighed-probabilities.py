import numpy as np
import pandas as pd
from utilities.plotting import plot_weighed_conditional_pairs

data2 = pd.read_csv('../data/raw/port_only_v4.csv')
data2 = data2.sort_values('count_joint', ascending=False)
data2.head()

max_sample_size_v4 = data2['count_joint'].max()
max_sample_size_v4
log_max_sample_size_v4 = np.log2(max_sample_size_v4)
log_max_sample_size_v4
log_avg_sample_size_v4 = np.log2(data2.head(3)['count_joint'].mean())
log_avg_sample_size_v4

data2['prob_weighed'] = data2['probability']* np.log2(data2['count_joint']) / log_avg_sample_size_v4
data2.head()

# plot both together in order of probabilites
# sort first
data2 = data2.sort_values('count_joint', ascending=False)
x2 = np.arange(len(data2))

plot_weighed_conditional_pairs(data2, ['port_b'], top_n=1000, title="IPv4 Weighed Conditional Probability P(port a | port b)",  sav_location="../figures/figure-2d-ipv4-weighed-probabilities")