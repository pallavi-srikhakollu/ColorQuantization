#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:59:23 2018

@author: Pallavi
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def classification(centers,points):
     color_set = []

     for point in points:
        dist = []
        for center in centers:
            dist.append( math.sqrt((center[0] - point[0])**2 + (center[1] - point[1])**2))
             
        ind = np.argmin(dist)
        color_set.append(ind)
     
     print("Points:",points)
     print("calsification vector:", color_set)
     
     return color_set
     
def plot_centers(centers):
    colors = ['red','green','blue']
    
    indx = 0
    for center in centers:
         plt.plot(center[0], center[1], 'o', color=colors[indx])
         s = "(" + str(center[0]) + "," + str(center[1]) +")"
         plt.text(center[0],center[1],s )
         indx += 1 
 
def plot_points(points,color_set):
     colors = ['red','green','blue']
     for i in range(0,len(points)):
         point = points[i]
         plt.scatter(point[0],point[1], marker='^', facecolor='none' ,edgecolor=colors[color_set[i]])
         s = "(" + str(point[0]) + "," + str(point[1]) +")"
         plt.text(point[0],point[1],s )
     
def plot_classify(centers,points):
    
    color_set = classification(centers,points)
    
    fig, ax = plt.subplots()
    rect = patches.Rectangle((4.5,2.6),0.5,0.2,linewidth=0,edgecolor='r',facecolor='none')
    ax.add_patch(rect)
     
    plot_centers(centers)
    plot_points(points,color_set)
    
    plt.savefig("Task3_iter1_a.png", dpi = 300)
    plt.close()

def task2(centers,points,fig_name):
     color_set = []
     red = [centers[0]]
     green = [centers[1]]
     blue = [centers[2]]
     
     for point in points:
         dist = []
         for center in centers:
            dist.append( math.sqrt((center[0] - point[0])**2 + (center[1] - point[1])**2))
             
         ind = np.argmin(dist)
         color_set.append(ind)
         
         if ind == 0:
            red.append(point)
         elif ind == 1:
            green.append(point)
         else:
            blue.append(point)
         
     red.sort(key=lambda t: t[0])
     green.sort(key=lambda t: t[0])
     blue.sort(key=lambda t: t[0])       
     
     new_center1 = [0,0]
     mean = np.mean(red,axis =0)
     new_center1[0] = np.round(mean[0],1)
     new_center1[1] = np.round(mean[1],1)
     
     new_center2 = [0,0]
     x,y = np.mean(green,axis =0)
     new_center2[0] = np.round(x,1)
     new_center2[1] = np.round(y,1)

     new_center3 = [0,0]
     mean = np.mean(blue,axis =0)
     new_center3[0] = np.round(mean[0],1)
     new_center3[1] = np.round(mean[1],1)     

     for i in red:
        if(np.array_equal(i,new_center1)):
            red.remove(i)
     for j in green:
        if(np.array_equal(j,new_center2)):
            green.remove(j)
     for k in blue:
        if(np.array_equal(k,new_center3)):
            blue.remove(k)
     
     fig, ax = plt.subplots()
     rect = patches.Rectangle((4.5,2.6),0.5,0.2,linewidth=0,edgecolor='r',facecolor='none')
     ax.add_patch(rect)
     point1 = []
     
     plot_centers([new_center1,new_center2,new_center3])
     for point in red:
         plt.scatter(point[0],point[1], marker='^', facecolor='none' ,edgecolor='r')
         s = "(" + str(point[0]) + "," + str(point[1]) +")"
         plt.text(point[0],point[1],s )
         point1.append(point)
         
     for point in green:
         plt.scatter(point[0],point[1], marker='^', facecolor='none' ,edgecolor='g')
         s = "(" + str(point[0]) + "," + str(point[1]) +")"
         plt.text(point[0],point[1],s )
         point1.append(point)
         
     for point in blue:
         plt.scatter(point[0],point[1], marker='^', facecolor='none' ,edgecolor='b')
         s = "(" + str(point[0]) + "," + str(point[1]) +")"
         plt.text(point[0],point[1],s )
         point1.append(point)
         
     plt.savefig(fig_name, dpi = 300)
     plt.close()
     print("Points:" ,point1)
     print("Classification vector:" ,color_set)
     return ([new_center1,new_center2,new_center3],point1)



def plot_classify2(centers1,points):
    
    color_set = classification(centers1,points)
    
    fig, ax = plt.subplots()
    rect = patches.Rectangle((4.5,2.6),0.5,0.2,linewidth=0,edgecolor='r',facecolor='none')
    ax.add_patch(rect)
     
    plot_centers(centers1)
    plot_points(points,color_set)
    
    plt.savefig("task3_iter2_a.png", dpi = 300)
    plt.close()


center1 = (6.2, 3.2)
center2 = (6.6, 3.7)
center3 = (6.5, 3.0)


points = [[5.9,3.2],[4.6,2.9],[6.2,2.8],[4.7,3.2],[5.5,4.2],[5.0,3.0],
     [4.9,3.1],[6.7,3.1],[5.1,3.8],[6.0,3.0]]

plot_classify([center1,center2,center3],points)
new_centers,points1 = task2([center1,center2,center3],points,"task3_iter1_b.png")
plot_classify2(new_centers,points1)
s = "task3_iter2_b.png"
task2(new_centers,points1,s)

    