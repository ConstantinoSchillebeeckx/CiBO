# collection of helper utilities for analysis

import seaborn as sns
from matplotlib import pyplot as plt    
import numpy as np
import pandas as pd
import os
import scipy.stats

# TODO - docs
def draw_hist(x, xlabel, ylabel, title, log=False):

    plt.figure(figsize=(17,4))

    if log: 
        x = np.log10(x)
        xlabel = xlabel + ' (log10 transformed)'

    ax = sns.distplot(x, kde=False)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.suptitle(title, fontsize=20)


# TODO - docs
def autosave_fig(notebook_name, root = '../../reports/figures/'):
    current_figs = [l for l in os.listdir(root) if notebook_name in l]
    count = len(current_figs)
    fig_name = "%s-%s.svg" %(notebook_name, count)
    fig_out = os.path.join(root, fig_name)
    plt.savefig(fig_out)
    print 'Figure %s saved.' %fig_out



def remove_outliers(x):

    assert isinstance(x, pd.Series), "must provide series object"

    q25, q75 = x.quantile([0.25,0.75]).tolist()
    iqr = q75 - q25
    min = q25 - (1.5 * iqr)
    max = q75 + (1.5 * iqr)

    return x[(x <= max) & (x >= min)]



def get_highest_rated_beers(df, n=5, score_col = 'review_overall', beer_id_col = 'beer_beerid'):
    '''
    Return a list of the n most highest rated beers from a dataframe

    Args:
        df (pandas dataframe): input data which includes scores for beers on each row
        n (int, optional): top n number of beers to return. Defaults to 3
        score_col (str, optional): name of column that contains score values. Defaults to review_overall
        beer_id_col (str, optional): name of column that identifies beers. Defaults to beer_beerid

    Yields:
        array of beer ids that are most highly rated. note that the length of this
        array is not guarenteed to be length n since, in the case of tied scores,
        the function will keep returning the next best beer until a different score
        is found.
    '''

    assert score_col in df.columns, "Col %s not found in input data" %score_col
    assert beer_id_col in df.columns, "Col %s not found in input data" %beer_id_col

    beers = []
    prev_score = 0

    # iterate over dataframe, grabbing highest rated beers
    for ix,row in df.sort_values(score_col, ascending=False).iterrows(): 
        beer = row[beer_id_col] 
        score = row[score_col]

        if len(beers) >= n and score != prev_score:
            break
    
        # keep score if we don't have enough beers, or the scores are tied    
        if len(beers) < n or score == prev_score:
            beers.append(beer)

        prev_score = score

    return beers


def split_data(df, ratios=[0.6,0.2,0.2], random=42):

    from sklearn.model_selection import train_test_split
    import numpy as np

    assert np.sum(ratios) == 1, "ratios array must sum to 1"

    a = ratios[0]
    b = ratios[1]/np.sum(ratios[1:])

    dat_train, dat_tmp = train_test_split(df, train_size=a, random_state=random)
    dat_cv, dat_test = train_test_split(dat_tmp, train_size=b, random_state=random)

    return dat_train, dat_cv, dat_test


