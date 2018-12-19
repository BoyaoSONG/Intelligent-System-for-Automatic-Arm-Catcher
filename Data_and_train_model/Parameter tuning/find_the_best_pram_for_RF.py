import xlrd
from sklearn.ensemble import RandomForestClassifier
from sklearn.grid_search import GridSearchCV

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

param_test1 =dict(n_estimators=list(range(10,71,10)))
gsearch1= GridSearchCV(estimator=RandomForestClassifier(min_samples_split=100,min_samples_leaf=20, max_depth=8, max_features='sqrt',random_state=10),
                       param_grid =param_test1,scoring='accuracy',cv=10)
gsearch1.fit(data_x,label_y)

print(gsearch1.best_score_)
print(gsearch1.best_params_)
print(gsearch1.best_estimator_)

"""
Result:
0.9092134831460674
{'n_estimators': 70}
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=8, max_features='sqrt', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=20, min_samples_split=100,
            min_weight_fraction_leaf=0.0, n_estimators=70, n_jobs=1,
            oob_score=False, random_state=10, verbose=0, warm_start=False)

"""