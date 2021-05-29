# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *
from matplotlib.pyplot import *
from cam_functions import *
from math import *
def shm_rise(shm_theta_rise_start,shm_theta_rise_end,shm_h_start,shm_h_end,RPM): #Input- Start Angle, End Angle, Initial Displacement, Final Displacement, cam shaft RPM
 if shm_theta_rise_start<shm_theta_rise_end and shm_h_start<shm_h_end: # Proceed if Start angle is smaller than End angle and Initial Displacement is lower than Final Displacement
  
  shm_tr=linspace(shm_theta_rise_start,shm_theta_rise_end,100) #Dividing the Cam Angle theta
  shm_beta_rise=(shm_theta_rise_end-shm_theta_rise_start)  #Angle Beta
  shm_h_rise=(shm_h_end-shm_h_start) #Displacement difference
  
  omega=degrees(2*pi*RPM/60) #Angular Velocity of Cam Shaft
  
  s_shm_rise=empty(len(shm_tr)) # Allocating empty array for Displacement of Cam Angle Theta
  v_shm_rise=empty(len(shm_tr)) # Allocating empty array for Velocity of Cam Angle Theta
  a_shm_rise=empty(len(shm_tr)) # Allocating empty array for Acceleration of Cam Angle Theta
  
  for sr in range(0,len(shm_tr)): # Looping the cam angles into equations
   s_shm_rise[sr]=shm_h_start+((shm_h_rise/2)*(1-cos(pi*((shm_tr[sr]-shm_theta_rise_start)/shm_beta_rise))))     #Displacement equation of the follower
   v_shm_rise[sr]=(((pi*omega)/shm_beta_rise)*(shm_h_rise/2)*sin(pi*(shm_tr[sr]-shm_theta_rise_start)/shm_beta_rise))     #Velocity equation of the follower
   a_shm_rise[sr]=(((pi*omega)**2)/(shm_beta_rise**2)*(shm_h_rise/2)*cos(pi*(shm_tr[sr]-shm_theta_rise_start)/shm_beta_rise)) #Acceleration equation of the follower
  
  return (shm_tr,s_shm_rise,v_shm_rise,a_shm_rise) # return Theta,Displacement,Velocity,Acceleration
 
 elif shm_theta_rise_start>=shm_theta_rise_end:# if Initial angle Theta  is greater than Final angle Theta
     return "Initial cam_angle should be smaller than final cam_angle " #return
 elif shm_h_start>=shm_h_end:# if Initial displacement is greater than Final displacement
     return "Initial displacement of follower must be smaller than final displacement" # return