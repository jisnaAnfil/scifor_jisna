# -*- coding: utf-8 -*-
"""MissingAndDuplicates.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17a8FX3jYcGgkJbg4uGXmx5dQIAJZq-ll
"""

!pip install kaggle

!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d slmsshk/medical-students-dataset

!unzip medical-students-dataset.zip

import pandas as pd
import numpy as np

df=pd.read_csv("medical_students_dataset.csv")

df.head()

df.info()

missing_values = df.isnull()
missing_values

"""**Dropping Missing Values:**|
Use dropna() to remove rows or columns with missing values.
Specify axis=0 to drop rows and axis=1 to drop columns.

**Filling Missing Values**:
Use fillna() to replace missing values with a specific value or a calculated value (e.g., mean, median).
"""

duplicates = df.duplicated()
duplicates

num_duplicates = df.duplicated().sum()
num_duplicates

