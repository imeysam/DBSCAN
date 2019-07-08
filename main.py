from Constant import Constant
from DBSCAN import DBSCAN
from sklearn import datasets

if __name__ == "__main__":
    dataset_type = input("Dataset type(Iris:1 or Local:2,3,4) :")
    dataset_type = int(dataset_type)

    clusters = []
    noises = []

    if dataset_type == Constant.IrisDataset:
        iris = datasets.load_iris()
        dataset = iris.data
        dbscan = DBSCAN(dataset, 0.39, 4)
        dbscan.run()
        clusters = dbscan.getClusters()
        noises = dbscan.getNoise()
    elif dataset_type == Constant.LocalFirstDataset:
        pass
    elif dataset_type == Constant.LocalSecondDataset:
        pass
    elif dataset_type == Constant.LocalThirdDataset:
        pass

    print("Cluster count: {}".format(len(clusters)))

    cluster_count = 0

    """Plot all data on a page"""
    for cluster in clusters:
        cluster_count += 1
        print("Cluster {}th: {}".format(cluster_count, len(cluster.points())))

    print("Noise count: {}".format(len(noises)))