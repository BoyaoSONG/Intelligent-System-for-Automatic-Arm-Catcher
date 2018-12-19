import xlrd
from sklearn.svm import SVC
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

clf = SVC()
tuned_parameters = [{'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]}
                   ]

grid = GridSearchCV(clf,tuned_parameters, cv=10, scoring='accuracy')
grid.fit(data_x,label_y)
# grid_mean_scores = [result.mean_validation_score for result in grid.grid_scores_]
# print(grid_mean_scores)

print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)

"""
Result:
0.91
{'C': 10, 'gamma': 0.001}
SVC(C=10, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

"""
