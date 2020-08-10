import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nba_allstar = pd.read_csv('nba_all_star_games.csv')

nba_allstar.head()
nba_allstar.shape

round1 = nba_allstar[nba_allstar.nba_draft_status.str.contains('Rnd 1')]
round1.shape

len(round1.player.unique())

round2 = nba_allstar[nba_allstar.nba_draft_status.str.contains('Rnd 2')]
round2.shape

len(round2.player.unique())

round3 = nba_allstar[~nba_allstar.nba_draft_status.str.contains('Rnd 1|Rnd 2')]
round3.shape

len(round3.player.unique())

round1.loc[round1['team'] == 'New York Knicks']
round2
round3
