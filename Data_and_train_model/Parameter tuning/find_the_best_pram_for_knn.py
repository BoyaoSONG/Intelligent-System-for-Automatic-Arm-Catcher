import xlrd
from sklearn.neighbors import KNeighborsClassifier
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

knn = KNeighborsClassifier()
k_range = list(range(1,101))

print(k_range)

prama_grid = dict(n_neighbors=k_range)

grid = GridSearchCV(knn, prama_grid, cv=10, scoring='accuracy')
grid.fit(data_x,label_y)
grid_mean_scores = [result.mean_validation_score for result in grid.grid_scores_]
print(grid_mean_scores)

print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)

"""
Result:
0.9061797752808989
{'n_neighbors': 30}
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=30, p=2,
           weights='uniform')

"""