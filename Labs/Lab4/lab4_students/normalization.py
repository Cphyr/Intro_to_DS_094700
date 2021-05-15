from point import Point
from numpy import mean, var


class DummyNormalizer:
    def fit(self, points):
        pass

    def transform(self, points):
        return points


class ZNormalizer:
    def __init__(self):
        self.mean_variance_list = []

    def fit(self, points):
        all_coordinates = [p.coordinates for p in points]
        self.mean_variance_list = []
        for i in range(len(all_coordinates[0])):
            values = [x[i] for x in all_coordinates]
            self.mean_variance_list.append(
                [mean(values), var(values, ddof=1)**0.5])

    def transform(self, points):
        self.fit(points)
        new = []
        for p in points:
            new_coordinates = p.coordinates
            new_coordinates = [(new_coordinates[i] - self.mean_variance_list[i][0]) / self.mean_variance_list[i][1]
                               for i in range(len(p.coordinates))]
            new.append(Point(p.name, new_coordinates, p.label))
        return new


class MinMaxNormalizer:
    def __init__(self):
        pass

    def transform(self, points):
        """"
        Params: 
            self: the MinMaxNormalizer object
            points: Iterable of Point objects
        Returns: 
            new_points: Iterable of Point objects. The coordinates of each points is the MinMax    
        """
        min_dic = {}  # dictionary of the min in the certain dimension
        max_dic = {}  # dictionary of the max in the certain dimension
        new_points = []  # creates the list for the new points
        # creates list of all coordinates
        all_coordinates = [p.coordinates for p in points]
        dimensions = len(all_coordinates[0])
        for i in range(dimensions):  # finds out the min and max in all of the dimensions
            values = [x[i] for x in all_coordinates]
            min_dic[i] = min(values)
            max_dic[i] = max(values)

        # calculates the min-max transformation and adds the new point to the list
        for i, p in enumerate(points):
            current = p.coordinates
            new_points.append(Point(p.name, [(current[i]-min_dic[i])/(max_dic[i]-min_dic[i])
                                             for i in range(dimensions)], p.label))
        return new_points


class SumNormalizer:
    def __init__(self):
        pass

    def transform(self, points):
        """
        :param points: Iterable() of Point() to be transformed
        :return: List() of Point()
        """
        new_points = []

        # Create list. Each elem is a list of the coordinates of each point
        all_coordinates = [p.coordinates for p in points]

        denoms = []  # list of the denominators of each dimention
        for i in range(len(all_coordinates[0])):
            vals = [x[i] for x in all_coordinates]
            denoms.append(sum(map(abs, vals)))

        num_dims = len(denoms)

        for p in points:  # Iterate of the points
            new_coor = []

            # Compute normilzed value of each coordinate
            for i in range(num_dims):
                new_coor.append(p.coordinates[i]/denoms[i])

            # Append to the new list of points
            new_points.append(Point(p.name, new_coor, p.label))

        return new_points
