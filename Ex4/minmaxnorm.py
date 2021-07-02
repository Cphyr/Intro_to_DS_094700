from point import *


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
