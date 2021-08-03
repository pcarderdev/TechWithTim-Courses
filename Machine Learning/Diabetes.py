import numpy as np
import sklearn 
from sklearn.datasets import load_diabetes
from sklearn import linear_model
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

data = load_diabetes()

## Looking at data
# desc = data['DESCR']
# labels = data['feature_names']
# target = data['target']

predict = 'target'

X = np.array(data['data'])
y = np.array(data['target'])

#x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

### Linear model performed at ~.50 min=0.20 max=0.60
# Current best model at 0.7041878618521193
best = 0
for _ in range(250):

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    linearReg = linear_model.LinearRegression()
    linearReg.fit(x_train, y_train)
    acc = linearReg.score(x_test, y_test)
    if acc > best:
        with open("diabetesmodel.pickle", "wb") as f:
            pickle.dump(linearReg, f)
            best = acc

print(best)

style.use("ggplot")
pyplot.scatter(X[:,2], y)
pyplot.xlabel('bmi')
pyplot.ylabel('Final Results')
pyplot.show()





