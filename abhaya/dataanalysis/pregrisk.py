import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn import preprocessing

feature_cols = ['worksi1f', 'cleanair', 'sporty1f', 'alcoholf', 'cancerf', 'menarche', 'avdaysp', 'infpro1f', 'ocs']
output_cols = ['WEIGHT',  'MODEDELIV', 'BABYCONDIT', 'Status']

data = pd.read_excel('/home/dell/Desktop/PALS_data.XLSX')
print data.head()

X = data.loc[:, feature_cols]
y = data.loc[:, output_cols]
print X.shape

le = preprocessing.LabelEncoder()
y.WEIGHT = le.fit_transform(y.WEIGHT)

le = preprocessing.LabelEncoder()
y.MODEDELIV = le.fit_transform(y.MODEDELIV)

le = preprocessing.LabelEncoder()
y.BABYCONDIT = le.fit_transform(y.BABYCONDIT)

le = preprocessing.LabelEncoder()
X.ocs = le.fit_transform(X.ocs)


clf = RandomForestClassifier(n_estimators=100, random_state=1)
#clf = svm.SVC(gamma=0.001, C=1000., kernel = 'linear')
multi_target_forest = MultiOutputClassifier(clf, n_jobs=-1)
multi_target_forest.fit(X, y)

print "success"
