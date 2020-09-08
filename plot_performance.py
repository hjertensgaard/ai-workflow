import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

def plot_performance_all_countries(log_file):
    df = pd.read_csv(log_file)

    df['rmse'] = [eval(df['eval_test'][index])['rmse'] for index in df['eval_test'].index]
    df['runtime_seconds'] = [datetime.datetime.strptime(df['runtime'][index][1:], "%H:%M:%S").second for index in
                             df['runtime'].index]

    model_versions = np.unique(df['model_version_note'])

    df_version_dict = {}

    for version in model_versions:
        df_version_dict[version] = get_performance_df(df, version)

    df_to_plot = df_version_dict[model_versions[0]]
    df_to_plot.columns = ['(from_date, to_date)', 'rmse_' + model_versions[0], 'runtime_' + model_versions[0]]
    for version in model_versions[1:]:
        df_to_plot['rmse_' + version] = df_version_dict[version]['rmse']
        df_to_plot['runtime_' + version] = df_version_dict[version]['runtime_seconds']

    columns = ['rmse_' + version for version in model_versions]
    ax = df_to_plot[columns].plot(kind='bar', title="Model Comparision", figsize=(15, 10), legend=True, fontsize=12)
    ax.set_xlabel("Country", fontsize=12)
    ax.set_ylabel("Rooted mean squared error", fontsize=12)
    plt.tight_layout()
    plt.show()

def get_performance_df(df, version):
    df_temp = df.loc[df['model_version_note'] == version]
    df_temp = df_temp.drop(['unique_id', 'timestamp', 'eval_test', 'runtime', 'model_version_note', 'model_version'],
                           axis=1)
    df_temp.index = df_temp['country']
    df_temp = df_temp.drop(['country'], axis=1)
    return df_temp

def main():
    plot_performance_all_countries('./logs/train-2020-9.log')


if __name__ == "__main__":
    main()
    plt.show()