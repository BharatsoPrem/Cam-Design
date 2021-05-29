# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *
from matplotlib.pyplot import *
from cam_functions import *
from math import *
def linear_rise(lin_theta_rise_start,lin_theta_rise_end,lin_h_rise_start,lin_h_rise_end,RPM):# Input- Start angle, End angle, Initial displacement, Final displacement, Cam Shaft RPM
  if lin_theta_rise_start<lin_theta_rise_end and lin_h_rise_start<lin_h_rise_end: # Proceed if Start angle is smaller than End angle and Initial Displacement is lower than Final displacement
    
    lin_h_rise=(lin_h_rise_end-lin_h_rise_start) #Displacement difference
    lin_tr=linspace(lin_theta_rise_start,lin_theta_rise_end,endpoint=1) #Dividing the Cam Angle theta
    lin_beta_rise=(lin_theta_rise_end-lin_theta_rise_start) #Angle Beta
    
    omega=degrees(2*pi*RPM/60) # Angular Velocity of Cam Shaft
    
    s_lin_rise=empty(len(lin_tr)) # Allocating empty array for Displacement of Cam Angle Theta
    v_lin_rise=empty(len(lin_tr)) # Allocating empty array for Velocity of Cam Angle Theta
    a_lin_rise=empty(len(lin_tr)) # Allocating empty array for Acceleration of Cam Angle Theta
    
    
    for lr in range(0,len(lin_tr)): # Looping the cam angles into equations
     s_lin_rise[lr]=(lin_h_rise*(lin_tr[lr]-lin_theta_rise_start)/lin_beta_rise)+lin_h_rise_start# Displacement equation of the follower
    v_lin_rise=((lin_h_rise*omega)/lin_beta_rise)*ones(len(lin_tr)) # Velocity equation of the follower
    a_lin_rise=zeros(len(lin_tr))                                   #Acceleration equation of the follower
    
    return (lin_tr,s_lin_rise,v_lin_rise,a_lin_rise) # return Theta,Displacement,Velocity,Acceleration
  
  elif lin_theta_rise_start>=lin_theta_rise_end: # If Initial angle Theta is greater than Final angle theta
     return "Initial cam_angle should be smaller than the final cam_angle." #return
  elif lin_h_rise_start>=lin_h_rise_end:         # If Initial displacement is higher than Final displacement
     return "Initial displacement must be smaller than the final displacement." # return