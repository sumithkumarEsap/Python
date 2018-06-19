import numpy as np
import matplotlib.pyplot as plt
import random
#creatig a cluster at the start like random one
def create_cluster(X, centroid_pts):
    cluster = {}
    for x in X:
        value = min([(i[0],np.linalg.norm(x - centroid_pts[i[0]]))for i in enumerate(centroid_pts)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster


#calculate new cluster value based on the centroid values found
def calculate_new_center(cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu

#comparing new and old centroids and if same then we can keep the centroid as the one
def matched(new_centroids, old_centroids):
    return (set([tuple(a)for a in new_centroids]) == set([tuple(a)for a in old_centroids]))


#runnig the k-mean algorithm on the data
def Apply_Kmeans(X, K, N):
    # selecting random centroids from dataset and by number of clusters.
    old_centroids = np.random.randint(N, size = K)
    old_centroid_pts = np.array([X[i]for i in old_centroids])

    print("old :",old_centroids)
    print(old_centroid_pts)

    cluster_info = create_cluster(X, old_centroid_pts)

    print("Initial cluster information:")
    print(cluster_info)
    new_centroid_pts=calculate_new_center(cluster_info)
    print("new :", new_centroid_pts)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    plot_cluster(old_centroid_pts,cluster_info,itr)
    #comparing the centroids and calculating for new centroid if not matched else keeping the centroid
    while not matched(new_centroid_pts, old_centroid_pts):
        itr = itr + 1
        old_centroid_pts = new_centroid_pts
        cluster_info = create_cluster(X,new_centroid_pts)
        plot_cluster(new_centroid_pts, cluster_info,itr)
        new_centroid_pts = calculate_new_center(cluster_info)

    print("Results after final iteration:")
    plot_cluster(new_centroid_pts, cluster_info, itr)#plotting the cluster
    return

#plotting the cluster
def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()

#plotting the graph
def init_graph(N, p1, p2):
    X = np.array([(random.choice(p1),random.choice(p2))for i in range(N)])
    return X

#intitialising the values for the cluster
def Simulate_Clusters():
    K = int(input('Enter the number of Clusters.......'))
    print('Running...\n')
    p1 = np.array([5.5,6,5.4,6.2,5,6.8,7,4,5,5.6,5.5,6.3])
    p2 = np.array([55,56,65,50,56,49,55,60,78,66,56,61])
    X = init_graph(len(p1), p2, p1)
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()
    Apply_Kmeans(X, K, len(X))#calling the function


if __name__ == '__main__':
    Simulate_Clusters()