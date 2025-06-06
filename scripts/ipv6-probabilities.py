import numpy as np
import pandas as pd
from utilities.plotting import plot_conditional_pairs

df_v4_ports = pd.read_csv('../data/raw/ports-unqiue-lzrv4.csv')
df_v6_ports = pd.read_csv('../data/raw/ports-unique-lzrv6.csv')
port_to_check = list(set(df_v4_ports['p']).intersection(set(df_v6_ports['p'])))

df1 = pd.read_csv('../data/raw/v6-conditional-probs-port-only-conditional.csv')
# filter out instances that take into account anything not in port_to_check
df1 = df1[df1['port_b'].isin(port_to_check)]
df1 = df1[df1['port_a'].isin(port_to_check)]
# filter out anything that is less than 0.00001
print(f"min: {min(df1['probability'])}")
print(f"max: {max(df1['probability'])}")
print(f"mean: {np.mean(df1['probability'])}")
print(f"median: {np.median(df1['probability'])}")
print(f"std: {np.std(df1['probability'])}")
df1 = df1[df1['probability'] > 0.0001]

# filter out anything with count_condition less than 50
print(f"min: {min(df1['count_condition'])}")
print(f"max: {max(df1['count_condition'])}")
print(f"mean: {np.mean(df1['count_condition'])}")
print(f"median: {np.median(df1['count_condition'])}")
print(f"std: {np.std(df1['count_condition'])}")

df1 = df1[df1['count_condition'] > 100]
df1.shape

plot_conditional_pairs(df1, ['port_b'], top_n=772, title = "IPv6 Conditional Probability P(port a | port b)", sav_location="../figures/figure-2a-ipv6-probabilities")