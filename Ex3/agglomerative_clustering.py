from cluster import *
from sample import compute_euclidean_distance as dist


def sample_in(sample, cluster):
    return sum([sample.dist(other) for other in cluster.samples])/(len(cluster.samples)-1)


def min_dist(sample, curr):
    return sum([sample.dist(other) for other in curr.samples])/len(curr.samples)


def sample_out(sample, clusters, curr):
    return min([min_dist(sample, c) for c in clusters if c != curr])


def silhouette(sam, clusters, curr):
    out_val = sample_out(sam, clusters, curr)
    in_val = sample_in(sam, curr)
    return (out_val - in_val)/max(out_val, in_val)


def are_in_same(first, second, clusters):
    for cluster in clusters:
        if (first in cluster and second in Cluster):
            return True
        if (first in cluster and not (second in Cluster)):
            return False
        if (not (first in cluster) and (second in Cluster)):
            return False


class Agglomerative_Cluster:
    def _init_(self, link, samples):
        """
        :params:
            :link: a Link object
            :samples: List() :: Samples()

        :return:
            constructor
        """
        self.link = link
        self.clusters = [Cluster(i + 1, sample)
                         for i, sample in enumerate(samples)]  # init each sample as a cluster

    def compute_silhoeutte(self):
        silh_dict = {}
        for clus in self.clusters:
            if len(clus.samples) == 1:
                silh_dict[clus.samples[0]] = 0
                continue
            for sam in clus.samples:
                silh_dict[sam.s_id] = silhouette(sam, self.clusters, clus)

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
        for i in range(num_of_samples-1):
            for j in range(i+1, num_of_samples):
                first = samples[i]
                second = samples[j]
                same_l = second.s_d == first.s_id
                same_c = are_in_same(first, second)
                if(same_l and same_c):
                    TP += 1
                elif(not same_l and not same_c):
                    TN += 1
                elif(not same_l and same_c):
                    FP += 1
                elif(same_l and not same_c):
                    FN += 1
        return (TP+TN)/(TP+TN+FP+FN)
