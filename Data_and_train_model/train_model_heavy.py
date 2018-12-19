import xlrd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC     # support vecter machine for classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.externals import joblib

workbook = xlrd.open_workbook("all.xls")
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
X_train, X_test, y_train, y_test = train_test_split(data_x,label_y,test_size=0.2)
model1 = KNeighborsClassifier(n_neighbors=30)
model2 = SVC(C=10,gamma=0.001,probability=True) # By default, probability is disable so svc can't do soft voting
model3 = RandomForestClassifier( n_estimators=70)
model4 = GaussianNB() # GaussianNB only has one parameters : probabilite of priors(先验概率)， by default is all samples， no need to change
model5 = DecisionTreeClassifier(criterion='entropy', max_depth=9, splitter='best')

#evc1 = VotingClassifier(estimators=[('model1',model1),('model2',model2),('model3',model3)],voting='hard')
#evc2 = VotingClassifier(estimators=[('model1',model2),('model2',model3),('model3',model4)],voting='soft')
#evc3 = VotingClassifier(estimators=[('model1',model3),('model2',model4),('model3',model5)],voting='hard')
#evc4 = VotingClassifier(estimators=[('model1',model4),('model2',model5),('model3',model1)],voting='hard')
#evc5 = VotingClassifier(estimators=[('model1',model5),('model2',model1),('model3',model2)],voting='hard')
#evc6 = VotingClassifier(estimators=[('model1',model1),('model2',model3),('model3',model4)],voting='hard')
#evc7 = VotingClassifier(estimators=[('model1',model2),('model2',model4),('model3',model5)],voting='hard')
#evc8 = VotingClassifier(estimators=[('model1',model3),('model2',model5),('model3',model1)],voting='soft')
#evc9 = VotingClassifier(estimators=[('model1',model4),('model2',model1),('model3',model2)],voting='soft')
#evc10 = VotingClassifier(estimators=[('model1',model2),('model2',model3),('model3',model5)],voting='hard')

'''
find the best voting mode for each evc
'''
# clf=[evc1,evc2,evc3,evc4,evc5,evc6,evc7,evc8,evc9,evc10]
# for i in clf:
#     param_test1 =[{'voting': ['hard','soft']}]
#     gsearch1= GridSearchCV(estimator=i,
#                            param_grid =param_test1,scoring='accuracy',cv=10)
#     gsearch1.fit(data_x,label_y)
#     print('************ Result for : ',i,'**************')
#     print(gsearch1.best_score_)
#     print(gsearch1.best_params_)
#     print(gsearch1.best_estimator_)

evc = VotingClassifier(estimators=[('model1',model1),('model2',model2),('model3',model3),('model4',model4),('model5',model5)],voting='hard')

evc.fit(data_x,label_y)

print(evc.score(X_test,y_test))
print(evc.predict([[355,91]]))
joblib.dump(evc,'/home/pi/Desktop/ISSAC/model/model_isaac.pkl')
