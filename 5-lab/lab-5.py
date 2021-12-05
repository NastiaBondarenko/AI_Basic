
import pandas as pd
from six import StringIO
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import datasets #here import data package
from sklearn.linear_model import LinearRegression # здесь используется метод регрессии
import matplotlib.pyplot as plt              
pima = pd.read_csv("playInfo.csv")

def forecast():
	global pima
	X = pima.iloc[:,:1]
	y = pima.iloc[:,1:]

	X_test = X.iloc[:1]

	clf = LinearRegression()
	clf = clf.fit(X, y)


	y_pred = clf.predict(X_test)

	pred = []

	for i in y_pred:
		pred.append([i[0], round(i[1]), round(i[2])])

	df2 = pd.DataFrame([[1, pred[0][0],pred[0][1],pred[0][2]]], columns=['algoritm','time','win', 'points'], index=[len(pima)])
	pima = pd.concat([pima, df2])

	

for i in range(5):
	forecast()

print(pima)

pima.to_csv('playForecast.csv', index=False) 

