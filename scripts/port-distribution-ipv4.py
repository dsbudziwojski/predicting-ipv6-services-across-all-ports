import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df3 = pd.read_csv('../data/raw/v6-deduped.csv')
# print(df3.head())

# plotting
df3 = df3.sort_values("freq", ascending=False).reset_index(drop=True)
top20 = df3.iloc[:30].copy()
others_sum = df3.iloc[30:]["freq"].sum()
others_row = pd.DataFrame({"port_number": ["Others"], "freq": [others_sum]})
top20 = pd.concat([top20, others_row], ignore_index=True)
plt.figure(figsize=(12,6))
bars = plt.bar(top20["port_number"].astype(str), top20["freq"])

plt.title("Top 30 Most Frequent Ports from LZR IPv6 Dataset")
plt.xlabel("Port Number")
plt.ylabel("Frequency of Port")
plt.xticks(rotation=45, ha="right")
for bar in bars:
    h = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        h + max(top20["freq"])*0.005,
        f"{int(h):,}",
        ha="center", va="bottom", fontsize=8, rotation=90
    )
plt.tight_layout()
plt.savefig("../figures/figure-1a-port_distribution_ipv6.png", dpi=300)
# plt.show() # uncomment to see

