from main import Point
from main import getleftmostPoint
from main import getrightmostPoint
import pytest

def test_getleftmostPoint():
    """ Testing getleftmostPoint() """
    point_list = [Point(1, 1), Point(3, 2), Point(4, 5)]
    leftmostPoint = getleftmostPoint(point_list)
    assert (leftmostPoint.xCoord, leftmostPoint.yCoord) == (1, 1)


def test_getrightmostPoint():
    """ Testing getrightmostPoint() """
    point_list = [Point(1, 1), Point(3, 2), Point(4, 5)]
    rightmostPoint = getrightmostPoint(point_list)
    assert rightmostPoint.xCoord == 4 and rightmostPoint.yCoord == 5
