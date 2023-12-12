from sklearn import datasets
from sklearn.linear_model  import LogisticRegression
iris = datasets.load_iris()
print(list(iris.keys()))
print(iris['data'][:,3:])
print(iris['target'] ==2)

 