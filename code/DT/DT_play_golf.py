"""
====================================================================
Decision trees on the play-golf dataset
====================================================================
Mahmood Amintoosi

"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
data = pd.read_csv('../dataset/playgolf.csv')

print(data)