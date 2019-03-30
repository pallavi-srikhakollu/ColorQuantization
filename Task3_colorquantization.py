#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 18:28:28 2018

@author: Pallavi
"""

import cv2
import math
import numpy as np
from numpy import mean

UBIT_NAME = "psrikhak"
np.random.seed(sum([ord(c) for c in UBIT_NAME]))
threshold = 20

#Refernce: https://stackoverflow.com/questions/26765875/python-pil-compare-colors/26768008
def luminance(pixel):
    return (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])

def is_similar(pixel_a, pixel_b, threshold): 
    print(abs(luminance(pixel_a) - luminance(pixel_b)))
    return abs(luminance(pixel_a) - luminance(pixel_b)) < threshold

def quantize_image(img_path,number_colors):
    img1 = cv2.imread(img_path)
    height,width,k  = img1.shape
    
    picked_colors = []
    new_color = []
    
    for i in range(0,number_colors):
        
        random_width = int(np.random.uniform(0,width-2,1))
        random_height = int(np.random.uniform(0,height-2,1))
        print(img1[random_width,random_height])
        color = img1[random_width,random_height]
        picked_colors.append(color)
        
    #Reading image another time
    img2 = cv2.imread(img_path)
    distances = []   
    
    color_sets = []
    for color in picked_colors:
        color_sets.append([color])
        
    
    is_threshold = True
    
    while is_threshold:
        new_color = []
        color_sets = []
        for color in picked_colors:
            color_sets.append([color])
        
        for x in range(0,height-2):
                for y in range(0,width-2):
                     pix_cor = img1[x,y]
                     distances = []
                     for k in range(0,len(picked_colors)):
                         r1,g1,b1 = picked_colors[k]
                         distances.append((math.sqrt((pix_cor[0] - r1)**2 + 
                                                            (pix_cor[1] - g1)**2 + 
                                                            (pix_cor[2] - b1)**2)))
                     
                     ind = np.argmin(distances)
                     rf,gf,bf = picked_colors[ind]
                     
                     for color_set_index in range(0,len(color_sets)):
                         if color_set_index == ind:
                             r,g,b = img1[x,y]
                             color_sets[color_set_index].append((r,g,b))
                             
                    
        for point_list in color_sets:         
            new_color.append(mean(point_list, axis=0))
       
        for index in range(0,len(picked_colors)):
            
            if is_similar(new_color[index],picked_colors[index] ,threshold ):
                is_threshold = False
            else:
                is_threshold = True
        
        if is_threshold == True:
            picked_colors = new_color
             
    #For coloring the image
    for x in range(0,height):
                for y in range(0,width):
                 
                     pix_cor = img1[x,y]
                     distances = []
                     for k in range(0,len(new_color)):
                         r1,g1,b1 = new_color[k]
                         distances.append((math.sqrt((pix_cor[0] - r1)**2 + 
                                                     (pix_cor[1] - g1)**2 + 
                                                     (pix_cor[2] - b1)**2)))
                         
                     ind = np.argmin(distances)
                 
                     rf,gf,bf = new_color[ind]
                     img2[x,y] = (rf,gf,bf)
    
    return img2


img3 =  quantize_image("/Users/Pallavi/Documents/Cvip_lab_2/data/baboon.jpg",3)
cv2.imwrite("task3_baboon_3.jpg",img3)
    
img4 =  quantize_image("/Users/Pallavi/Documents/Cvip_lab_2/data/baboon.jpg",5)
cv2.imwrite("task3_baboon_5.jpg",img4)
            
img5 =  quantize_image("/Users/Pallavi/Documents/Cvip_lab_2/data/baboon.jpg",10)
cv2.imwrite("task3_baboon_10.jpg",img5)

img6 =  quantize_image("/Users/Pallavi/Documents/Cvip_lab_2/data/baboon.jpg",20)
cv2.imwrite("task3_baboon_20.jpg",img6)
            
    