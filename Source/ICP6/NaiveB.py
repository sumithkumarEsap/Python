from sklearn import naive_bayes, metrics
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_predict

#loading the data into irisdataset
irisdataset = datasets.load_iris()

# getting the data and response of the dataset
x = irisdataset.data
y = irisdataset.target

#creating an instance

my_model= GaussianNB()
#aplitting the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#fitting the training data on my_model by using .fit function()
my_model.fit(x_train,y_train)
#predicting on the test data by calling the predict function
y_pred = my_model.predict(x_test)

#getting the accuracy score
print(metrics.accuracy_score(y_test, y_pred))



