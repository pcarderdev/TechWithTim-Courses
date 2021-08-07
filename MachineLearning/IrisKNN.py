import sklearn
from sklearn.datasets import load_iris
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

data = load_iris()

desc = data["DESCR"]

X = np.array(data.data[:,:1])
y = np.array(data.target)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size =0.1)

#KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
acc = knn.score(x_test, y_test)
print(acc)

predicted = knn.predict(x_test)
names = ['Setosa', 'Versicolour', 'Virginica']

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], " Actual: ", names[y_test[x]])
