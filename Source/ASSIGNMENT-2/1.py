from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


irisdataset = datasets.load_iris()
x = irisdataset.data
y = irisdataset.target

model = LinearDiscriminantAnalysis()
model.fit(x, y)
print(x)
print(model.predict([[1, 2, 3, 4], [2, 3, 4, 5]]))
print(model.score(x, y))

