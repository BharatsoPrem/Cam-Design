# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *
from matplotlib.pyplot import *
from cam_functions import *
from math import *
def uar_rise(uar_theta_rise_start,uar_theta_rise_end,uar_h_rise_start,uar_h_rise_end,RPM): # Input- Start angle, End angle, Initial displacement, Final displacement, cam shaft RPM
   
   if uar_theta_rise_start<uar_theta_rise_end and uar_h_rise_start<uar_h_rise_end: # Proceed if start angle is greater than end angle and initial displacement is lower than final displacement  
    
    uar_beta_rise=(uar_theta_rise_end-uar_theta_rise_start)  #Angle Beta     
    uar_h_rise=(uar_h_rise_end-uar_h_rise_start)             #Displacement difference
    uar_theta_mid_rise=((uar_theta_rise_start+uar_theta_rise_end)/2) # Mid-value of Cam angle theta
    
    uar_tr1=linspace(uar_theta_rise_start,uar_theta_mid_rise,endpoint=0) #Dividing the first half of cam angle theta 
    uar_tr2=linspace(uar_theta_mid_rise,uar_theta_rise_end,endpoint=1)   #Dividing the second half of cam angle theta 
    
    omega=degrees(2*pi*RPM/60)  #Angular velocity of Cam Shaft
    
    s_uar_rise1=empty(len(uar_tr1)) # Allocating empty array for displacement for first half of cam angle theta  
    v_uar_rise1=empty(len(uar_tr1)) # Allocating empty array for velocity for first half of cam angle theta
    
    s_uar_rise2=empty(len(uar_tr2)) # Allocating empty array for displacement for second half of cam angle theta
    v_uar_rise2=empty(len(uar_tr2)) # Allocating empty array for velocity for second half of cam angle theta
    
    for ur1 in range(0,len(uar_tr1)): # Looping first half of cam angles into equations   
     s_uar_rise1[ur1]=uar_h_rise_start+(2*uar_h_rise*((uar_tr1[ur1]-uar_theta_rise_start)/uar_beta_rise)**2) # Displacement equation for first half of cam angles
     v_uar_rise1[ur1]=(4*uar_h_rise*omega)*((uar_tr1[ur1]-uar_theta_rise_start)/(uar_beta_rise)**2)  # velocity equation for first half of cam angles
    a_uar_rise1=(4*uar_h_rise*(omega**2))/((uar_beta_rise)**2)*ones(len(uar_tr1)) # acceleration equation for first half of cam angles
    
    for ur2 in range(0,len(uar_tr2)): # Looping second half of cam angles into equations
     s_uar_rise2[ur2]=uar_h_rise_start+((uar_h_rise)*(1-2*(1-(uar_tr2[ur2]-uar_theta_rise_start)/uar_beta_rise)**2)) # Displacement equation for second half of cam angles
     v_uar_rise2[ur2]=((4*uar_h_rise*omega)/uar_beta_rise)*(1-((uar_tr2[ur2]-uar_theta_rise_start)/uar_beta_rise)) # Velocity equation for second half of cam angles
    a_uar_rise2=(-(4*uar_h_rise*(omega**2))/((uar_beta_rise)**2)*ones(len(uar_tr2))) # Acceleration equation for second half of cam angles
    
    uar_tr=hstack((uar_tr1,uar_tr2))            # Concatenating first half and second half of theta values 
    s_uar_rise=hstack((s_uar_rise1,s_uar_rise2)) # Concatenating first half and second half of displacement values
    v_uar_rise=hstack((v_uar_rise1,v_uar_rise2)) # Concatenating first half and second half of velocity values   
    a_uar_rise=hstack((a_uar_rise1,a_uar_rise2)) # Concatenating first half and second half of acceleration values
    #plot(uar_tr,s_uar_rise)
    return (uar_tr,s_uar_rise,v_uar_rise,a_uar_rise) # return Theta,Displacement,Velocity,Acceleration 
   
   elif uar_theta_rise_start>=uar_theta_rise_end: # if initial theta angle is greater than final theta angle  
     return "Initial cam_angle should be smaller than the final cam_angle." # return
   elif uar_h_rise_start>=uar_h_rise_end: # if initial displacement is greater than final displacement
     return "Initial displacement must be smaller than the final displacement." # return