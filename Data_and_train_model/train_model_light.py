import xlrd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC     # support vecter machine for classifier
import matplotlib.pyplot as plt
from sklearn.externals import joblib
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier

workbook = xlrd.open_workbook("/home/pi/Desktop/ISSAC/all.xls")
sheet = workbook.sheet_by_index(0)
data_x = []
label_y = []

# 找有多少行数据
rows = sheet.nrows
cols = sheet.ncols
for i in range(1,rows):
    x1 = sheet.cell_value(i,0)
    y1 = sheet.cell_value(i,1)
    y = sheet.cell_value(i,2)

    data_x.append([x1,y1])
    label_y.append(y)

    i = i+1
X_train, X_test, y_train, y_test = train_test_split(data_x,label_y,test_size=0.3)

model1 = GaussianNB()
model2 = SVC(C=10,gamma=0.001,probability=True)
model3 = KNeighborsClassifier(n_neighbors=30)
evc = VotingClassifier(estimators=[('model1',model1),('model2',model2),('model3',model3)],voting='hard')
evc.fit(data_x,label_y)
print(evc.score(X_test,y_test))
print(evc.predict([[351,91]]))


joblib.dump(evc,'/home/pi/Desktop/ISSAC/model/model_light.pkl')
