## Creates k centroids
## Straws straight line between each centroid
## Find average of each cluster
## Repeats until there is no difference between the centroids and the average of the cluster

## Very high time cost, #points * #centroids * #iterations_it_takes * #features

import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics

digits = load_digits()
data = scale(digits.data)
y = digits.target

k = len(np.unique(y))

samples, features = data.shape

##TODO Figure out what these different metrics mean
def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
        % (name, estimator.inertia_,
        metrics.homogeneity_score(y, estimator.labels_),
        metrics.completeness_score(y, estimator.labels_),
        metrics.v_measure_score(y, estimator.labels_),
        metrics.adjusted_rand_score(y, estimator.labels_),
        metrics.adjusted_mutual_info_score(y, estimator.labels_),
        metrics.silhouette_score(data, estimator.labels_, metric='euclidean')))

'''
https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation
Homogeneity score - each cluster contains only members of a single class (0.0-1.0) 
Completeness score - all members of a given class are assigned to the same cluster (0.0-1.0)
V_measure score - harmonic mean of homogeneity and completeness, B defaults to 1.0 (beta=)
                    v = ((1 + B) x homogeneity x completeness) /
                        (B x homogeneity + completeness)
Adjusted Rand score - 
Adjusted Mutual Info score - 
Silhouette score - 
'''

clf = KMeans(n_clusters=k, init='random', n_init=10)
bench_k_means(clf, "1", data)
