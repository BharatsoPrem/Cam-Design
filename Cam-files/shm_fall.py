# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *
from matplotlib.pyplot import *
from cam_functions import *
from math import *
def shm_fall(shm_theta_fall_start,shm_theta_fall_end,shm_h_fall_start,shm_h_fall_end,RPM): #Input- Start Angle, End Angle, Initial Displacement, Final Displacement, RPM
 if shm_theta_fall_start<shm_theta_fall_end and shm_h_fall_start>shm_h_fall_end: # Proceed if Start angle is smaller than End angle and Initial Displacement is higher than Final Displacement
  
  shm_tf=linspace(shm_theta_fall_start,shm_theta_fall_end,100) #Dividing the Cam Angle theta
  shm_beta_fall=(shm_theta_fall_end-shm_theta_fall_start) #Angle Beta
  shm_h_fall=(-shm_h_fall_end+shm_h_fall_start) #Displacement difference
  
  omega=degrees(2*pi*RPM/60) #Angular Velocity of Cam Shaft
  
  s_shm_fall=empty(len(shm_tf)) # Allocating empty array for Displacement of Cam Angle Theta
  v_shm_fall=empty(len(shm_tf)) # Allocating empty array for Velocity of Cam Angle Theta
  a_shm_fall=empty(len(shm_tf)) # Allocating empty array for Acceleration of Cam Angle Theta
  
  for sf in range(0,len(shm_tf)): # Looping the cam angles into equations
   s_shm_fall[sf]=shm_h_fall_start-((shm_h_fall/2)*(1-cos(pi*((shm_tf[sf]-shm_theta_fall_start)/shm_beta_fall))))     #Displacement equation of the follower
   v_shm_fall[sf]=-((pi*omega/shm_beta_fall)*(shm_h_fall/2)*sin(pi*(shm_tf[sf]-shm_theta_fall_start)/shm_beta_fall))   #Velocity equation of the follower
   a_shm_fall[sf]=-(((pi*omega)**2)/(shm_beta_fall**2)*(shm_h_fall/2)*cos(pi*(shm_tf[sf]-shm_theta_fall_start)/shm_beta_fall)) #Acceleration equation of the follower
  
  return shm_tf,s_shm_fall,v_shm_fall,a_shm_fall # return Theta,Displacement,Velocity,Acceleration
 
 elif shm_theta_fall_start>=shm_theta_fall_end: # If Initial Theta Angle is greater than Final Theta Angle
     return "Initial cam_angle should be smaller than the final cam_angle " #return 
 elif shm_h_fall_start<=shm_h_fall_end:         # If Initial displacement is smaller than Final displacement
     return "Initial displacement must be higher than the final displacement" # return