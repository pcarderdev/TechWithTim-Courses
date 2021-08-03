## Support Vector Machine
# Classification 
import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_breast_cancer()
#print(cancer.feature_names)
#print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)
classes = ["malignant", "benign"]

## Hyper-plane - a plane between the two datasets where the closest point is equal distance from the plane (infinite number of planes, what's the best one?)
# Best hyper-plane is maximum distance from the two closest points
# Area between sets called the margin (want to maximize)

# Use 'kernels' for bad data sets
# kernel = f(x1, x2) -> x3

# clf = svm.SVC(kernel="linear", C=1)
clf = KNeighborsClassifier(n_neighbors=13)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)
print(acc)

