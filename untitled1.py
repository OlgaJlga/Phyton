# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19yWA4DpJSqK8Nx4tzmOXD4df8PPSBRII
"""

!pip --version

!pip install pandas

import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder

from sklearn.preprocessing import LabelEncoder

import random
lst_R = ['robot'] * 10
lst_H = ['human'] * 10
random.shuffle(lst)
data.loc[data.whoAmI == 'robot', 'id'] = 0
data.loc[data.whoAmI == 'human', 'id'] = 1
label_encoder = LabelEncoder().fit(data.whoAmI)
data['id'] = label_encoder.transform(data.whoAmI)
data.head()