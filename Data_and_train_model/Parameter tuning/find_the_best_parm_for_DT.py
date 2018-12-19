import xlrd
from sklearn.tree import DecisionTreeClassifier
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

criterion_options = ['gini','entropy']
splitter_options = ['best','random']
max_depth = list(range(1, 10))
param_griddtree = dict(criterion=criterion_options,splitter=splitter_options,max_depth=max_depth)
gsearch1 = GridSearchCV(DecisionTreeClassifier(random_state=0),param_grid=param_griddtree,cv=10,scoring='accuracy')
gsearch1.fit(data_x,label_y)

print(gsearch1.best_score_)
print(gsearch1.best_params_)
print(gsearch1.best_estimator_)
"""
0.9030337078651686
{'criterion': 'entropy', 'max_depth': 9, 'splitter': 'best'}
DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=9,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=0,
            splitter='best')

"""
