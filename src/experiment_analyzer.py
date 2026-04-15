import pandas as pd, numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

class ExperimentAnalyzer:
    def __init__(self, df):
        self.df=df
        self.c=df[df.variant=='control']
        self.t=df[df.variant=='treatment']

    def analyze(self, col, t):
        c=self.c[col]; t2=self.t[col]
        if t=='proportion':
            z,p=proportions_ztest([c.sum(),t2.sum()],[len(c),len(t2)])
        else:
            _,p=stats.ttest_ind(t2,c)
        return {
            "metric":col,
            "control":c.mean(),
            "treatment":t2.mean(),
            "lift":(t2.mean()-c.mean())/c.mean(),
            "p":p
        }
