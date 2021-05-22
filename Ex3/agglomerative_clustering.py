from cluster import *
from sample import *
import math
from collections import OrderedDict
from link import *


def are_in_same(first, second, clusters):
    for cluster in clusters:
        samps = cluster.samples
        if (first in samps and second in samps):
            return True
        if (first in samps and not (second in samps)):
            return False
        if (not (first in samps) and (second in samps)):
            return False


def get_dist_of_pairs(samples):
    dists_dict = {}
    for i, first in enumerate(samples):
        for second in samples[i:]:
            dists_dict[str(sorted([first.s_id, second.s_id]))
                       ] = first.compute_euclidean_distance(second)
    return dists_dict


def pair_2_key(first, second):
    sort_pair = sorted([first, second], key=lambda x: x.c_id)
    new_first = sort_pair[0]
    new_second = sort_pair[1]
    return f"{new_first.c_id} {new_first.length} {new_second.c_id} {new_second.length}"


def get_dist_of_all_clusters(link, clusters, pairs_dist):
    clusters_dist = {}
    for i, first in enumerate(clusters[:-1]):
        for second in clusters[i+1:]:
            clusters_dist[pair_2_key(first, second)] = link.compute(
                first, second, pairs_dist, clusters_dist)
    return clusters_dist


class Agglomerative_Cluster:
    def __init__(self, link, samples):
        """
        :params:
            :link: a Link object
            :samples: List() :: Samples()

        :return:
            constructor
        """
        self.link = link
        self.samples = samples
        self.clusters = [Cluster(sam.s_id, [sam])
                         for sam in samples]  # init each sample as a cluster

        self.pairs_dist = get_dist_of_pairs(samples)
        self.clusters_dist = get_dist_of_all_clusters(
            link, self.clusters, self.pairs_dist)

    def distance(self, first, second):
        return self.pairs_dist[str(sorted([first.s_id, second.s_id]))]

    def sample_in(self, sam, cluster):
        return sum([self.distance(sam, other) for other in cluster.samples])/(len(cluster.samples)-1)

    def dist_sample_cluster(self, sam, curr):
        return sum([self.distance(sam, other) for other in curr.samples])/len(curr.samples)

    def sample_out(self, sam, clusters, curr):
        return min([self.dist_sample_cluster(sam, c) for c in clusters if c != curr])

    def silhouette(self, sam, clusters, curr):
        out_val = self.sample_out(sam, clusters, curr)
        in_val = self.sample_in(sam, curr)
        return (out_val - in_val)/max(out_val, in_val)

    def compute_silhoeutte(self):

        silh_dict = {}
        for clus in self.clusters:
            if len(clus.samples) == 1:
                silh_dict[clus.samples[0].s_id] = 0
                continue
            for sam in clus.samples:
                silh_dict[sam.s_id] = self.silhouette(sam, self.clusters, clus)
        return silh_dict

    def compute_summery_silhoeutte(self):
        """
        :returns:
            dict where each key is a c_id and the corr value is the silh of the cluster
            the value of the key 0 is the total silh of the clusterting
        """
        sum_silh_dict = {}
        silh_dict = self.compute_silhoeutte()  # get all silh
        all_silh = []  # will store all the silhs of all clusers

        # go over clusters
        for clus in self.clusters:
            # get a list of silhs of current cluster
            curr_silh = [silh_dict[x.s_id] for x in clus.samples]
            # add to the dict the avg silh in the current cluster
            sum_silh_dict[clus.c_id] = sum(curr_silh) / len(curr_silh)
            # combine lists
            all_silh += curr_silh
        # add to the dict the avg silh of all the data
        sum_silh_dict[0] = sum(all_silh) / len(all_silh)
        return sum_silh_dict

    def compute_rand_index(self):
        TP = TN = FP = FN = 0
        samples = []
        for clus in self.clusters:
            for sam in clus.samples:
                samples.append(sam)

        num_of_samples = len(samples)
        for i, first in enumerate(self.samples[:-1]):
            for second in self.samples[i+1:]:
                same_l = (second.label == first.label)
                same_c = are_in_same(first, second, self.clusters)
                if(same_l and same_c):
                    TP += 1
                elif(not same_l and not same_c):
                    TN += 1
                elif(not same_l and same_c):
                    FP += 1
                elif(same_l and not same_c):
                    FN += 1
        return (TP+TN)/(TP+TN+FP+FN)

    def run(self, max_clusters):
        number_of_clusters = len(self.clusters)
        if(max_clusters > number_of_clusters):
            return -1

        while(number_of_clusters > max_clusters):
            tup = min([(x, y, self.link.compute(x, y, self.pairs_dist, self.clusters_dist)) for i, x in enumerate(
                self.clusters) for y in self.clusters[i+1:]], key=lambda x: x[-1])
            tup[0].merge(tup[1])
            self.clusters.remove(tup[1])
            number_of_clusters -= 1

        self.clusters.sort(key=lambda x: x.c_id)
        print("complete link")

        s_dict = self.compute_summery_silhoeutte()
        for cluster in self.clusters:
            cluster.print_details(s_dict[cluster.c_id])
        print(
            f"Whole data: silhouette = {s_dict[0]:.3f} RI= {self.compute_rand_index():.3f}")
