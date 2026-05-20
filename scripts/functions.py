import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter

mtc_colors = {
    'Equity Priority Community':     '#fb2739',
    'Non-Equity Priority Community': '#285b8e'
}

def plot_distribution_and_mean_ci(
    df, y_col, x_col, title_prefix, x_label,
    y_label_boxplot, y_label_pointplot, filename_prefix,
    palette, ylim_multiplier=1.1
):
    """
    Saves a boxplot and a 95% CI point plot for any numeric column
    split by a categorical column. Returns list of saved filenames.

    Args:
        df               : DataFrame
        y_col            : numeric column to plot (e.g. 'pct_zvhhs')
        x_col            : categorical column to split by (e.g. 'type')
        title_prefix     : shown in chart titles
        x_label          : x-axis label
        y_label_boxplot  : y-axis label for boxplot
        y_label_pointplot: y-axis label for CI plot
        filename_prefix  : prefix for saved .png filenames
        palette          : dict mapping category → color
        ylim_multiplier  : headroom above max value (default 1.1)

    Example:
        plot_distribution_and_mean_ci(
            df=ac_zvhhs, y_col='pct_zvhhs', x_col='type',
            title_prefix='Zero Vehicle Households',
            x_label='Tract Type',
            y_label_boxplot='Proportion Without a Vehicle',
            y_label_pointplot='Proportion ZVH',
            filename_prefix='alameda_zvhhs',
            palette=mtc_colors
        )
    """
    generated_files = []
    df_clean = df.copy()
    df_clean[y_col] = pd.to_numeric(df_clean[y_col], errors='coerce')
    df_clean = df_clean.dropna(subset=[y_col, x_col])

    # Box plot
    fig_bx, ax_bx = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=x_col, y=y_col, data=df_clean,
                hue=x_col, palette=palette, legend=False, ax=ax_bx)
    ax_bx.set_title(f'Distribution of {title_prefix}\nIn Alameda County Census Tracts')
    ax_bx.set_xlabel(x_label)
    ax_bx.set_ylabel(y_label_boxplot)
    ax_bx.set_ylim(0, df_clean[y_col].max() * ylim_multiplier)
    ax_bx.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    bx_filename = f'{filename_prefix}_{y_col}_bxplot.png'
    plt.savefig(bx_filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig_bx)
    generated_files.append(bx_filename)

    # Point plot (mean + 95% CI)
    fig_pt, ax_pt = plt.subplots(figsize=(6, 4))
    sns.pointplot(data=df_clean, x=x_col, y=y_col, hue=x_col,
                  errorbar=('ci', 95), linestyle='none', capsize=0.2,
                  palette=palette, legend=False, ax=ax_pt)
    ax_pt.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax_pt.set_ylabel(y_label_pointplot)
    ax_pt.set_xlabel(x_label)
    ax_pt.set_title(f'Average Share of {title_prefix}\nBy {x_label} with 95% CI')
    plt.tight_layout()
    pt_filename = f'{filename_prefix}_{y_col}_95CI.png'
    plt.savefig(pt_filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig_pt)
    generated_files.append(pt_filename)

    return generated_files
