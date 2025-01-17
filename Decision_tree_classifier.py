import joblib
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.externals import joblib
from sklearn import tree




music_data = pd.read_csv('music.csv')
X = music_data.drop(columns='genre')
y = music_data['genre']
# # X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.2)
#
#
#
model = DecisionTreeClassifier()
model.fit(X,y)
# model = joblib.load('music-recommender.joblib')
tree.export_graphviz(model,out_file='music-recommender.dot', feature_names=['age','gender'],class_names=sorted(y.unique()),label='all',rounded=True,filled=Tru)



predictions = model.predict([[21,1]])
print (predictions)

# score = accuracy_score(y_test,predictions)
# print('Accuracy score is', score)