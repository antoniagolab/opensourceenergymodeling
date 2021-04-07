import numpy as np


class Point:
    """ 2D point class """
    def __init__(self, xCoord = 0, yCoord = 0):
        """
        initialization of point class
        :param xCoord: x-coordinate
        :param yCoord: y-coordinate
        """
        self.xCoord = xCoord
        self.yCoord = yCoord


def getleftmostPoint(listofpoints):
    """
    function to get leftmost point from multiple points
    :param listofpoints: list of objects of class Point; must be of length > 0
    :return: Point with smallest xCoord-value
    """
    xs = [p.xCoord for p in listofpoints]
    min_indx = np.argmin(xs)
    return listofpoints[min_indx]


def getrightmostPoint(listofpoints):
    """
    function to get rightmost point from multiple points
    :param listofpoints: list of objects of class Point; must be of length > 0
    :return: Point with highest xCoord-value
    """
    xs = [p.xCoord for p in listofpoints]
    max_indx = np.argmax(xs)
    return listofpoints[max_indx]
