import numpy as np
import pandas as pd
from utilities.plotting import plot_conditional_pairs

df_v4_ports = pd.read_csv('../data/raw/ports-unqiue-lzrv4.csv')
df_v6_ports = pd.read_csv('../data/raw/ports-unique-lzrv6.csv')
port_to_check = list(set(df_v4_ports['p']).intersection(set(df_v6_ports['p'])))

df5 = pd.read_csv('../data/raw/port_only_v4.csv')
df5 = df5[df5['port_b'].isin(port_to_check)]
df5 = df5[df5['port_a'].isin(port_to_check)]
df5 = df5[df5['probability'] > 0.00001]
df5 = df5[df5['count_condition'] > 100_000]

plot_conditional_pairs(df5,['port_b'],top_n=15,title="Top 15 IPv4 Conditional Probability P(port a | port b)",x_tick=True,sav_location="../figures/figure-3a-ipv4-top-15.png")
