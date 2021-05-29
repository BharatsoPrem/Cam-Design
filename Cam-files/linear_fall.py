# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *
from matplotlib.pyplot import *
from cam_functions import *
from math import *
def linear_fall(lin_theta_fall_start,lin_theta_fall_end,lin_h_fall_start,lin_h_fall_end,RPM): # Input- Start angle, End angle, Initial displacement, Final displacement, RPM
  if lin_theta_fall_start<lin_theta_fall_end and lin_h_fall_start>lin_h_fall_end: # Proceed if Start angle is smaller than End angle and Initial Displacement is higher than Final displacement
    
    lin_h_fall=(lin_h_fall_start-lin_h_fall_end)  #Displacement difference
    lin_tf=linspace(lin_theta_fall_start,lin_theta_fall_end,endpoint=1) #Dividing the Cam Angle theta
    lin_beta_fall=(lin_theta_fall_end-lin_theta_fall_start)  #Angle Beta
    
    
    omega=degrees(2*pi*RPM/60) #Angular velocity of Cam shaft 
    
    s_lin_fall=empty(len(lin_tf)) # Allocating empty array for Displacement of Cam Angle Theta
    v_lin_fall=empty(len(lin_tf)) # Allocating empty array for Velocity of Cam Angle Theta
    a_lin_fall=empty(len(lin_tf)) # Allocating empty array for Acceleration of Cam Angle Theta
    
    for lf in range(0,len(lin_tf)): # Looping the cam angles into equations
     s_lin_fall[lf]=lin_h_fall_start-(lin_h_fall*(lin_tf[lf]-lin_theta_fall_start)/lin_beta_fall)# Displacement equation of the follower
    v_lin_fall=-((lin_h_fall*omega)/lin_beta_fall)*ones(len(lin_tf)) # Velocity equations of the follower
    a_lin_fall=zeros(len(lin_tf))                      #Acceleration equation of the follower
    
    return (lin_tf,s_lin_fall,v_lin_fall,a_lin_fall) # return Theta,Displacement,Velocity,Acceleration
  
  elif lin_theta_fall_start>=lin_theta_fall_end:  # If Initial angle Theta is greater than Final Theta Angle
     return "Initial cam_angle should be smaller than the final cam_angle." #return
  elif lin_h_fall_start<=lin_h_fall_end:          # If Initial displacement is lesser than Final displacement
     return "Initial displacement must be higher than the final displacement." # return