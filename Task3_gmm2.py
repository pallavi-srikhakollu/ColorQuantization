#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 18:15:25 2018

@author: Pallavi
"""

import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

#Refered from: https://github.com/joferkington/oost_paper_code/blob/master/error_ellipse.py
def plot_cov_ellipse(cov, pos, nstd=2, ax=None, **kwargs):
    """
    Plots an `nstd` sigma error ellipse based on the specified covariance
    matrix (`cov`). Additional keyword arguments are passed on to the 
    ellipse patch artist.
    Parameters
    ----------
        cov : The 2x2 covariance matrix to base the ellipse on
        pos : The location of the center of the ellipse. Expects a 2-element
            sequence of [x0, y0].
        nstd : The radius of the ellipse in numbers of standard deviations.
            Defaults to 2 standard deviations.
        ax : The axis that the ellipse will be plotted on. Defaults to the 
            current axis.
        Additional keyword arguments are pass on to the ellipse patch.
    Returns
    -------
        A matplotlib ellipse artist
    """ 
    def eigsorted(cov):
        vals, vecs = np.linalg.eigh(cov)
        order = vals.argsort()[::-1]
        return vals[order], vecs[:,order]

    if ax is None:
        ax = plt.gca()
        

    vals, vecs = eigsorted(cov)
    theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
    print(theta)
    # Width and height are "full" widths, not radius
    width, height = 2 * nstd * np.sqrt(vals)
    ellip = Ellipse(xy=pos, width=width, height=height, angle=theta, **kwargs)
    
    ax.add_artist(ellip)
    return ellip


def calculate_gmm_model():
    colors = ['red','green','blue']
    eruptions = np.genfromtxt('old-faithful.csv', delimiter=',', skip_header=1, usecols=(1))
    waiting = np.genfromtxt('old-faithful.csv', delimiter=',', skip_header=1, usecols=(2))

    point_set = []

    for i in range(0,len(eruptions)):
        point_set.append([eruptions[i],waiting[i]])
    
    cov = np.array([
            [[1.30, 13.98], [13.98,184.82]],
            [[1.30, 13.98], [13.98,184.82]],
            [[1.30, 13.98], [13.98,184.82]]
            ])
    median_array = [ (4.0, 81),(2.0, 57),(4.0, 71)]
    
    pi_array = [0.333,0.333,0.333]
    prob_array = []
    
    
    for i in range(0,5):
        prob_array = []
        itert =0
        
        for median in median_array:
            a1 = cov[0][0]
            a2 = cov[0][1]
            
            new_cov1 = [a1[0],a1[1]],[a2[0],a2[1]]
            
            prob_array.append(multivariate_normal.pdf(point_set,median,new_cov1))
            itert +=1
            
        respon_array = []
        cluster_count = 0
        for cluster in prob_array:
            responsibility = []
            
            for index in range(0,len(cluster)):
                  prob_1 = pi_array[cluster_count] * cluster[index]
                  sum_prob = 0
                
                  for clusters in prob_array:
                      sum_prob += (pi_array[cluster_count] * clusters[index])
                      
                  responsibility.append(prob_1 / sum_prob)
            print("New responsibility arrya:")
            print(responsibility)
            cluster_count+=1
            respon_array.append(responsibility)  
            
        color_set = []
        for index1 in range(0,len(point_set)):
            resp_set = []
            for resp in respon_array:
                responsbility = resp[index1]
                resp_set.append(responsbility)
                     
            ind = np.argmax(resp_set)
            color_set.append(ind)
        #Calculation of new medians
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
        
        #calculations of new standard deviations
        cluster_count = 0
        new_deviation = []
        sum_res1 = []
        for cluster in respon_array:
                sum_x = 0
                sum_y = 0
                sum_res_dev = 0
               
                for idx in range(0,len(cluster)):
                    sum_res_dev += cluster[idx]
                    sum_x += (cluster[idx] * (abs(point_set[idx][0] - new_median[cluster_count][0])))
                    sum_y += (cluster[idx] * (abs(point_set[idx][1] - new_median[cluster_count][1])))
                    
                
                new_deviation.append([sum_x/sum_res_dev,sum_y/sum_res_dev])
                sum_res1.append(sum_res_dev)
                cluster_count+=1
                       
        #calculations of new weights         
        new_pi_array = []
        
        for cluster in respon_array:
                sum_res = 0
                for idx in range(0,len(cluster)):
                    sum_res += cluster[idx]
                
                new_pi_array.append(sum_res/len(cluster))
         
        pi_array = new_pi_array 
        
        new_cov = []
        tp = 0
        for deviation in new_deviation:
            print()
            
            print(deviation)
            
            cov1 = np.transpose(deviation)
            cov1 = np.convolve(cov1,deviation)
            a1 = float(np.round(cov1[0],2))
            
            b1 = float(np.round(cov1[1],2))
            c1 = float(np.round(cov1[2],2))
            print(b1)
            covet = np.array([[a1,b1],[b1,c1]])
            print(covet)
            min_eig = np.min(np.real(np.linalg.eigvals(covet)))
            if min_eig < 0:
                  covet -= 10*min_eig * np.eye(*covet.shape)
            new_cov.append(covet)
            tp+=1     
        median_array = new_median
       
        for s in range(0,len(point_set)):
         x, y = point_set[s]
         plt.scatter(x,y, marker='o', facecolor='none' ,edgecolor=colors[color_set[s]])
    
         
        plot_cov_ellipse(cov[0],median_array[0] , nstd=1,ax = None, alpha=0.5, color='red')
        plot_cov_ellipse(cov[1],median_array[1] , nstd=1, alpha=0.5, color='green')
        plot_cov_ellipse(cov[2],median_array[2] , nstd=1  ,alpha=0.5, color='blue')
        s = "task3_gmm_iter" + str(i) + ".jpg"
        plt.savefig(s, dpi = 300)
        plt.close()
        cov = new_cov
        print("---------------")
        print("New Covariance:")
        print(cov)
        print("---------------")
        print("Classificaion vector: 0 red , 1 green,2 blue")
        print(color_set)
        
calculate_gmm_model()