import sys
import pandas as pd
from link import *
from data import Data
from agglomerative_clustering import Agglomerative_Cluster


def main(argv):
    #data = Data(argv[1])
    data = Data("Leukemia_sample.csv")
    # Creates a single link and complete link object
    single = SingleLink()
    complete = CompleteLink()
    max_clus = 7

    for link in [single, complete]:
        # Loops through both of the links and runs agglomerative clustering
        agg_clus = Agglomerative_Cluster(link, data.create_samples())
        agg_clus.run(max_clus)
        if link == single:
            print()


if __name__ == "__main__":
    main(sys.argv)
