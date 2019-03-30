#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 06:50:46 2018

@author: Pallavi
"""

import Task3_colorquantization
import Task3_1
import Task3_gmm2
import cv2
import Project2_task3_gmm_1


#Calls for 1st to 3rd subtask
center1 = (6.2, 3.2)
center2 = (6.6, 3.7)
center3 = (6.5, 3.0)


points = [[5.9,3.2],[4.6,2.9],[6.2,2.8],[4.7,3.2],[5.5,4.2],[5.0,3.0],
     [4.9,3.1],[6.7,3.1],[5.1,3.8],[6.0,3.0]]

Task3_1.plot_classify([center1,center2,center3],points)
new_centers,points1 = Task3_1.task2([center1,center2,center3],points,"task3_iter1_b.png")
Task3_1.plot_classify2(new_centers,points1)
s = "task3_iter2_b.png"
Task3_1.task2(new_centers,points1,s)


#calls for 4th subtask(Image quantization)
img3 =  Task3_colorquantization.quantize_image("/Users/Pallavi/Documents/Cvip_lab_2/data/baboon.jpg",3)
cv2.imwrite("task3_baboon_3.jpg",img3)
    
img4 =  Task3_colorquantization.quantize_image("/Users/Pallavi/Documents/Cvip_lab_2/data/baboon.jpg",5)
cv2.imwrite("task3_baboon_5.jpg",img4)
            
img5 =  Task3_colorquantization.quantize_image("/Users/Pallavi/Documents/Cvip_lab_2/data/baboon.jpg",10)
cv2.imwrite("task3_baboon_10.jpg",img5)

img6 =  Task3_colorquantization.quantize_image("/Users/Pallavi/Documents/Cvip_lab_2/data/baboon.jpg",20)
cv2.imwrite("task3_baboon_20.jpg",img6)
            

#Calls for 5th Bonus part 1 subsub task. Calculating new mean using the
Project2_task3_gmm_1.gmm_modeling()

#Calls for 5th Bonus part 2 subsub task
Task3_gmm2.calculate_gmm_model()

