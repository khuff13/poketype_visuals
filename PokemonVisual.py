# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:36:50 2019

@author: krystinsteelman
"""

import PokemonAnalytics as PA
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


off_list_2 = PA.off_list_2_2
labels = list(PA.enum_list.keys())
poke_list_2 = PA.off_list_2

def_list_2 = PA.def_list_2
db_def_list_2 = pd.DataFrame.from_dict(def_list_2, orient = 'index')
db_def_list_2 = db_def_list_2.reset_index().rename(index = str, columns = {0:'count','index':'pokemon'})

db_poke_list_2 = pd.DataFrame.from_dict(poke_list_2, orient = 'index')
db_poke_list_2 = db_poke_list_2.reset_index().rename(index = str, columns = {0:'count','index':'pokemon'})

sns.set_style('darkgrid')
ax = sns.barplot(x = 'pokemon',y = 'count',data = db_poke_list_2)
plt.xticks(rotation = 'vertical')

sns.set_style('darkgrid')
ax = sns.barplot(x = 'pokemon',y = 'count',data = db_def_list_2)
plt.xticks(rotation = 'vertical')

sns.set_style('darkgrid')
ax = sns.distplot(off_list_2)
#ax.set_xticklabels(labels, rotation = 90)