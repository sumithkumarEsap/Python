import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#reading the data using pandas intovariables
variables = pandas.read_csv('sample_stocks.csv')
#storing 'returns' into y
Y = variables[['returns']]
#storing 'dividendyields into 'x'
X = variables[['dividendyield']]
#normalising the x,y to get into a linear form so that it will be easily analysed
X_norm = (X - X.mean()) / (X.max() - X.min())
Y_norm = (Y - Y.mean()) / (Y.max() - Y.min())

#finding the number of clusters
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
#kmeans
#storing the results into score
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
#score

#plotting the elbove cure to determine the number of clusters
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()

#principle component analysis
pca = PCA(n_components=1).fit(Y)
pca_d = pca.transform(Y)
pca_c = pca.transform(X)

#ploting the kmeans results by giving the number of clustes as 3
kmeans=KMeans(n_clusters=3)
kmeansoutput=kmeans.fit(Y)
#kmeansoutput
pl.figure('3 Cluster K-Means')
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')
pl.ylabel('Returns')
pl.title('3 Cluster K-Means')
pl.show()