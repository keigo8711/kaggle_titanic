import pandas as pd


class NA_fillar:
    def confirm_na_num(self, df: pd.DataFrame):
        print('-- Start confirmation --')
        print(df.isnull().sum())
    
    def fill_by_median(self, df: pd.DataFrame, target_feature: str, referred_feature: list) -> pd.DataFrame:
        df[target_feature] = df.groupby(referred_feature, group_keys=False)[target_feature].apply(lambda row : row.fillna(row.median()))
        return df