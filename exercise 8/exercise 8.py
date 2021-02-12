# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:34:04 2021

I use a very simple package that does everything we need, it is specifically 
designed to be used with coordinates, so it accounts for the Earth's curvature
automatically when constructing a polygon.

@author: Daniel Broderick
"""
# pip install sphericalpolygon
# this package works well with minimal dependencies
from sphericalpolygon import create_polygon
import numpy as np
 


def main(points, pt):
    """ format of points is as follows:
        [[42, -72], [45, -65], [lat, long]]
        pt should be [lat, long]

    """
    # simply make the polygon and check if it contains the point
    georange = create_polygon(np.array(points)) 
    out = georange.contains_points(pt) 
    print(out)
    return out



if __name__ == "__main__": 
    main([[10, 30],
          [0, 50],
         [0, 10]],
         [10,130])
        #[5, 25]  inside/true
        # [10, 130] outside/false