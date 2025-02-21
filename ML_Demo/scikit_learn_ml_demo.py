from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot


iris = datasets.load_iris()

# Extract X and Y matrix from loaded data
X_iris, y_iris = iris.data, iris.target
print(X_iris.shape, y_iris.shape)
print(X_iris[0], y_iris[0])

# Get dataset with only 2 features
X, y = X_iris[:, :2], y_iris

# Split the dataset into train and test sets. Test set will be 25%.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
print(X_train.shape, y_train.shape)

# Feature Scaling
fscaler = preprocessing.StandardScaler().fit(X_train)
X_train = fscaler.transform(X_train)
X_test = fscaler.transform(X_test)

# Plot the feature graph
colors = ['red', 'yellowgreen', 'blue']
for i in range(len(colors)):
    xaxs = X_train[:, 0][y_train == i]
    yaxs = X_train[:, 1][y_train == i]
    plot.scatter(xaxs, yaxs, c=colors[i])


plot.legend(iris.target_names)
plot.xlabel('Sepal Length')
plot.ylabel('Sepal Width')