#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
match_code = '392203'

def create_runs_series(match_code):
    runs = pd.Series(ipl_matches_array[:,16], index=ipl_matches_array[:,11])
    return runs

create_runs_series(match_code)
