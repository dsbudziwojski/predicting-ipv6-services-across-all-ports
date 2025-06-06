import matplotlib.pyplot as plt
import numpy as np

def plot_conditional_pairs(
    df,
    B_cols,
    count_col='count_condition',
    prob_col='probability',
    top_n=40,
    figsize=(15, 5),
    cmap='viridis',
    title=None,
    x_tick=False,
    sav_location="",
):
    df_plot = df.sort_values(count_col, ascending=False).head(top_n).copy()

    counts = df_plot[count_col]
    norm = plt.Normalize(vmin=counts.min(), vmax=counts.max())
    colors = plt.get_cmap(cmap)(norm(counts))

    fig, ax = plt.subplots(figsize=figsize)

    ax.bar(np.arange(len(df_plot)), df_plot[prob_col], color=colors)

    labels = []
    for i in range(len(df_plot)):
        left = ", ".join(str(df_plot[col].iloc[i]) for col in B_cols)
        right = str(df_plot['port_a'].iloc[i])
        labels.append(f"{left} → {right}")
    if x_tick:
      ax.set_xticks(np.arange(len(df_plot)))
      ax.set_xticklabels(labels, rotation=90, fontsize=8)



    ax.set_xlabel("port b → port a")
    # ax.set_xlabel(f"{', '.join(B_cols)}")
    ax.set_ylabel("Probability")
    ax.set_title(f"{title}")

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label="Sample Size")

    plt.tight_layout()
    plt.savefig(sav_location,dpi=300)

    return fig, ax



def plot_weighed_conditional_pairs(
    df,
    B_cols,
    count_col='count_condition',
    prob_col='prob_weighed',
    top_n=40,
    figsize=(15, 5),
    cmap='viridis',
    title=None,
    x_tick=False,
    sav_location=""
):
    df_plot = df.sort_values(count_col, ascending=False).head(top_n).copy()

    counts = df_plot[count_col]
    norm = plt.Normalize(vmin=counts.min(), vmax=counts.max())
    colors = plt.get_cmap(cmap)(norm(counts))

    fig, ax = plt.subplots(figsize=figsize)

    ax.bar(np.arange(len(df_plot)), df_plot[prob_col], color=colors)

    labels = []
    for i in range(len(df_plot)):
        left = ", ".join(str(df_plot[col].iloc[i]) for col in B_cols)
        right = str(df_plot['port_a'].iloc[i])
        labels.append(f"{left} → {right}")
    if x_tick:
      ax.set_xticks(np.arange(len(df_plot)))
      ax.set_xticklabels(labels, rotation=90, fontsize=8)

    ax.set_xlabel("port b → port a")
    # ax.set_xlabel(f"{', '.join(B_cols)}")
    ax.set_ylabel("Probability")
    ax.set_title(f"{title}")

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label="Sample Size")

    plt.tight_layout()
    plt.savefig(sav_location,dpi=300)

    return fig, ax
