#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:04:09 2018

@author: Pallavi
"""
import numpy as np
from scipy.stats import multivariate_normal

def gmm_modeling():
    
    point_set = np.array([[5.9,3.2],[4.6,2.9],[6.2,2.8],[4.7,3.2],[5.5,4.2],[5.0,3.0],
     [4.9,3.1],[6.7,3.1],[5.1,3.8],[6.0,3.0]])

    cov = np.array([[0.5, 0.0], [0.0,0.5]])
    median_array = [ (6.2, 3.2),(6.6, 3.7),(6.5, 3.0)]
    
    pi_array = [0.333,0.333,0.333]
    prob_array = []
    
    for median in median_array:
        prob_array.append(multivariate_normal.pdf(point_set,median,cov))
        
    respon_array = []
    
    for cluster in prob_array:
        responsibility = []
        
        for index in range(0,len(cluster)):
              prob_1 = pi_array[0] * cluster[index]
              sum_prob = 0
              i = 0
              for clusters in prob_array:
                  sum_prob += (0.333 * clusters[index])
                  i+=1
              responsibility.append(prob_1 / sum_prob)
        
        respon_array.append(responsibility)  
    
    new_median = []
    
    for cluster in respon_array:
        sum_x = 0
        sum_y = 0
        sum_res = 0
        for idx in range(0,len(cluster)):
            sum_x += (cluster[idx] * point_set[idx][0])
            sum_y += (cluster[idx] * point_set[idx][1])
            sum_res += cluster[idx]
        
        new_median.append((sum_x/sum_res,sum_y/sum_res))
    
    print(new_median)   