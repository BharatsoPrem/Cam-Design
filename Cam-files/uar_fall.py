# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *
from matplotlib.pyplot import *
from cam_functions import *
from math import *
def uar_fall(uar_theta_fall_start,uar_theta_fall_end,uar_h_fall_start,uar_h_fall_end,RPM): # Input- Start angle, End angle, Initial displacement, Final displacement, cam shaft RPM
  
   if uar_theta_fall_start<uar_theta_fall_end and uar_h_fall_start>uar_h_fall_end:# Proceed if Start angle is smaller than End angle and Initial displacement is higher than final displacement
    
    uar_beta_fall=(uar_theta_fall_end-uar_theta_fall_start) #Angle Beta
    uar_h_fall=(uar_h_fall_start-uar_h_fall_end)            #Displacement difference
    uar_theta_mid=((uar_theta_fall_start+uar_theta_fall_end)/2) # Mid-value of Cam angle theta
    
    uar_tf1=linspace(uar_theta_fall_start,uar_theta_mid,endpoint=0) #Dividing the first half of cam angle theta
    uar_tf2=linspace(uar_theta_mid,uar_theta_fall_end,endpoint=1) #Dividing the second half of cam angle theta
    
    omega=degrees(2*pi*RPM/60) #Angular velocity of Cam Shaft
    
    s_uar_fall1=empty(len(uar_tf1)) # Allocating empty array for displacement for first half of cam angle theta
    v_uar_fall1=empty(len(uar_tf1)) # Allocating empty array for velocity for first half of cam angle theta

    
    s_uar_fall2=empty(len(uar_tf2)) # Allocating empty array for displacement for second half of cam angle theta
    v_uar_fall2=empty(len(uar_tf2)) # Allocating empty array for velocity for second half of cam angle theta
    
    for uf1 in range(0,len(uar_tf1)): # Looping first half of cam angles into equations
     s_uar_fall1[uf1]=uar_h_fall_start-(2*uar_h_fall*((uar_tf1[uf1]-uar_theta_fall_start)/uar_beta_fall)**2) # Displacement equation for first half of cam angles
     v_uar_fall1[uf1]=-(4*uar_h_fall*omega)*((uar_tf1[uf1]-uar_theta_fall_start)/(uar_beta_fall)**2) # Velocity equation for first half of cam angles
    a_uar_fall1=-(4*uar_h_fall*(omega**2))/((uar_beta_fall)**2)*ones(len(uar_tf1))  # Acceleration equation for second half of cam angles
    
    for uf2 in range(0,len(uar_tf2)): # Looping second half of cam angles into equations
     s_uar_fall2[uf2]=uar_h_fall_start-((uar_h_fall)*(1-2*(1-(uar_tf2[uf2]-uar_theta_fall_start)/uar_beta_fall)**2)) # Displacement equation for second half of cam angles
     v_uar_fall2[uf2]=-((4*uar_h_fall*(omega))/uar_beta_fall)*(1-((uar_tf2[uf2]-uar_theta_fall_start)/uar_beta_fall)) # Velocity equation for second half of cam angles
    a_uar_fall2=-(-(4*uar_h_fall*(omega**2))/((uar_beta_fall)**2)*ones(len(uar_tf2))) # Acceleration equation for second half of cam angles
    
    uar_tf=hstack((uar_tf1,uar_tf2))  # Concatenating first half and second half of theta values
    s_uar_fall=hstack((s_uar_fall1,s_uar_fall2)) # Concatenating first half and second half of displacement values
    v_uar_fall=hstack((v_uar_fall1,v_uar_fall2)) # Concatenating first half and second half of velocity values
    a_uar_fall=hstack((a_uar_fall1,a_uar_fall2)) # Concatenating first half and second half of acceleration values
    #plot(uar_tf,s_uar_fall)
    return (uar_tf,s_uar_fall,v_uar_fall,a_uar_fall) # return Theta,Displacement,Velocity,Acceleration
   elif uar_theta_fall_start>=uar_theta_fall_end: # if initial angle theta is greater than final angle theta 
     return "Initial cam_angle should be smaller than the final cam_angle." # return
   elif uar_h_fall_start<=uar_h_fall_end: # if initial displacement is lesser than final displacement
     return "Initial displacement must be higher than the final displacement." # return