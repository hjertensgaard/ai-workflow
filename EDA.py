
import cslib
import pandas as pd
import matplotlib.pyplot as plt

def plot_summary_all_countries(df):
    pivot_table = pd.pivot_table(df['all'], index='year_month', values=['purchases', 'revenue', 'total_views'],
                                 aggfunc='sum').round(3)
    ax = pivot_table.plot(figsize=(15, 7))
    ax.set_xlabel("Year_month", fontsize=12)
    ax.set_title('Summary All countries')
    plt.tight_layout()
    plt.show()


def plot_summary_for_country(df, country):
    pivot_table = pd.pivot_table(df[country], index='year_month',
                                 values=['purchases', 'revenue', 'total_views'],
                                 aggfunc='sum').round(3)
    ax = pivot_table.plot(figsize=(15, 7))
    ax.set_xlabel("Year_month", fontsize=12)
    ax.set_title('Summary ' + country)
    plt.tight_layout()
    plt.show()


def get_pivot_table_from_country(df, country):
    return pd.pivot_table(df[country], index='year_month', values=['purchases', 'revenue', 'total_views'], aggfunc='sum').round(3)


def make_tables(df):
    first_country = list(df.keys())[0]
    pivot_table = get_pivot_table_from_country(df, first_country)

    revenue_df = pivot_table[['revenue', 'purchases']]
    revenue_df.columns = [first_country, 'to_drop']
    purchase_df = pivot_table[['purchases', 'revenue']]
    purchase_df.columns = [first_country, 'to_drop']
    total_views_df = pivot_table[['total_views', 'purchases']]
    total_views_df.columns = [first_country, 'to_drop']

    for idx, country in enumerate(df.keys()):
        if country != 'all' and idx > 0 and country != 'united_kingdom':
            pivot_table = get_pivot_table_from_country(df, country)
            revenue_df[country] = pivot_table['revenue']
            purchase_df[country] = pivot_table['purchases']
            total_views_df[country] = pivot_table['total_views']

    revenue_df.pop('to_drop')
    purchase_df.pop('to_drop')
    total_views_df.pop('to_drop')
    return revenue_df, purchase_df, total_views_df

def plot_revenue_for_all_but_united_kingdom(df):
    ax = df.plot(kind='bar', title="Revenue", figsize=(15, 10), legend=True, fontsize=12)
    ax.set_xlabel("Year_month", fontsize=12)
    ax.set_ylabel("Revenue", fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_purchases_for_all_but_united_kingdom(df):
    ax = df.plot(kind='bar', title="Purchases", figsize=(15, 10), legend=True, fontsize=12)
    ax.set_xlabel("Year_month", fontsize=12)
    ax.set_ylabel("Purchases", fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_total_views_for_all_but_united_kingdom(df):
    ax = revenue_df.plot(kind='bar', title="Total views", figsize=(15, 10), legend=True, fontsize=12)
    ax.set_xlabel("Year_month", fontsize=12)
    ax.set_ylabel("Total Views", fontsize=12)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = cslib.fetch_ts('./cs-train')
    plot_summary_all_countries(df)

    revenue_df, purchase_df, total_views_df = make_tables(df)
    plot_purchases_for_all_but_united_kingdom(purchase_df)