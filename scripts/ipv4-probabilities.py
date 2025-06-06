import numpy as np
import pandas as pd
from utilities.plotting import plot_conditional_pairs

df_v4_ports = pd.read_csv('../data/raw/ports-unqiue-lzrv4.csv')
df_v6_ports = pd.read_csv('../data/raw/ports-unique-lzrv6.csv')
port_to_check = list(set(df_v4_ports['p']).intersection(set(df_v6_ports['p'])))

df5 = pd.read_csv( '../data/raw/port_only_v4.csv')
df5

# filter out instances that take into account anything not in port_to_check
df5 = df5[df5['port_b'].isin(port_to_check)]
df5 = df5[df5['port_a'].isin(port_to_check)]
df5

# filter out anything that is less than 0.00001
print(f"min: {min(df5['probability'])}")
print(f"max: {max(df5['probability'])}")
print(f"mean: {np.mean(df5['probability'])}")
print(f"median: {np.median(df5['probability'])}")
print(f"std: {np.std(df5['probability'])}")

df5 = df5[df5['probability'] > 0.0001]
df5

# filter out anything with count_condition less than 50
print(f"min: {min(df5['count_condition'])}")
print(f"max: {max(df5['count_condition'])}")
print(f"mean: {np.mean(df5['count_condition'])}")
print(f"median: {np.median(df5['count_condition'])}")
print(f"std: {np.std(df5['count_condition'])}")

df5 = df5[df5['count_condition'] > 100_000]
df5

plot_conditional_pairs(df5, ['port_b'], top_n=1000, title="IPv4 Conditional Probability P(port a | port b)", sav_location="../figures/figure-2c-ipv4-probabilities")