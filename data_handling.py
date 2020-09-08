
import cslib

df = cslib.fetch_ts('/Users/andreashjertensgaard/Desktop/AI workflow examples/ai-workflow-capstone-master/cs-train')

for country, df_country in df.items():
    print(country, sum(df_country['revenue']))


df['united_kingdom']

from model import model_train

model = model_train('/Users/andreashjertensgaard/Desktop/AI workflow examples/ai-workflow-capstone-master/cs-train')

import pandas as pd
pd.pivot_table(df['all'], index='year_month', values=['purchases', 'revenue', 'total_views'], aggfunc='mean').round(3)

## YOUR CODE HERE

from monitoring import get_latest_train_data, get_monitoring_tools

## load latest data
data = get_latest_train_data()
y = data['y']
X = data['X']

## generate some data
bs_samples = 60
subset_indices = np.random.choice(np.arange(X.shape[0]),
                                  bs_samples,replace=True).astype(int)
mask = np.in1d(np.arange(X.shape[0]),subset_indices)
X_bs=X[mask]
X_outliers = X[:5].copy()
X_outliers['age'] = [88,90,76,80,68]
X_outliers['num_streams'] = [111,100,80,90,150]
X_query = pd.concat([X_bs,X_outliers])

print(X_query.shape)

import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('logs/train-2020-9.log')

df['rmse'] = [eval(df['eval_test'][index])['rmse'] for index in df['eval_test'].index]
df['runtime_seconds'] = [datetime.datetime.strptime(df['runtime'][index][1:], "%H:%M:%S").second for index in df['runtime'].index]

df.pop('unique_id')
df.pop('timestamp')
df.pop('eval_test')
df.pop('runtime')
df.pop('model_version_note')
df.pop('model_version')
df.index = df['country']
axes = df.plot.bar(rot=0, subplots=True)
axes[1].legend(loc=2)
labels =
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()