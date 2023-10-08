##########################################
# Light GBM
##########################################


import matplotlib.pyplot as plt
import pandas as pd
import MyPackege as mp


if __name__ == '__main__':

    # load the titanic data
    train = pd.read_csv('/workspaces/kaggle_titanic2/src/train.csv')
    test = pd.read_csv('/workspaces/kaggle_titanic2/src/test.csv')

    null_checker = mp.NA_fillar()
    null_checker.confirm_na_num(train)
    null_checker.confirm_na_num(test)

    train = null_checker.fill_by_median(df = train,
                                        target_feature = 'Age',
                                        referred_feature = ['Sex', 'Pclass'])
    null_checker.confirm_na_num(train)
    