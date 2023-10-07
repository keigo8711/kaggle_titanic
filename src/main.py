##########################################
# EDA
##########################################


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy


if __name__ == '__main__':
    print('Hello world!')

    # load the titanic data
    train = pd.read_csv('/workspaces/kaggle_titanic2/src/train.csv')
    test = pd.read_csv('/workspaces/kaggle_titanic2/src/test.csv')

    print('Survived: %d' % sum(train['Survived'] == 1))
    print('Non-survived: %d' % sum(train['Survived'] == 0))

    sns.catplot(x='Survived', col='Sex', kind='count', data=train)
    plt.savefig('/workspaces/kaggle_titanic2/result/eda1.png')
    cross_df_sex = pd.crosstab(train['Sex'], train['Survived'])
    print(cross_df_sex)
    _, p, _, _ = scipy.stats.chi2_contingency(cross_df_sex)
    print('P-value is %.4g' % p)