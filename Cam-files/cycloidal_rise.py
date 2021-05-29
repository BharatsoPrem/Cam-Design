# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *
from matplotlib.pyplot import *
from cam_functions import *
from math import *
def cycloidal_rise(cyc_theta_rise_start,cyc_theta_rise_end,cyc_h_rise_start,cyc_h_rise_end,RPM):#Input- Start Angle, End Angle, Initial Displacement, Final Displacement, Cam shaft RPM
 if cyc_theta_rise_start<cyc_theta_rise_end and cyc_h_rise_end>cyc_h_rise_start: # Proceed if Start angle is smaller than End angle and Initial Displacement is lower than Final displacement
  cyc_tr=linspace(cyc_theta_rise_start,cyc_theta_rise_end,100) #Dividing the Cam Angle theta
  cyc_beta_rise=(cyc_theta_rise_end-cyc_theta_rise_start)  #Angle Beta
  cyc_h_rise=(cyc_h_rise_end-cyc_h_rise_start) #Displacement difference
  
  omega=degrees(2*pi*RPM/60) # Angular Velocity of Cam Shaft
  
  s_cyc_rise=empty(len(cyc_tr))  # Allocating empty array for Displacement of Cam Angle Theta
  v_cyc_rise=empty(len(cyc_tr))  # Allocating empty array for Velocity of Cam Angle Theta
  a_cyc_rise=empty(len(cyc_tr))  # Allocating empty array for Acceleration of Cam Angle Theta
  
  for cr in range(0,len(cyc_tr)): # Looping the cam angles into equations
   s_cyc_rise[cr]=cyc_h_rise_start+(cyc_h_rise/pi)*(((pi*(cyc_tr[cr]-cyc_theta_rise_start)/(cyc_beta_rise))-((1/2)*sin(2*pi*((cyc_tr[cr]-cyc_theta_rise_start)/cyc_beta_rise)))))  #Displacement equation of the follower
   v_cyc_rise[cr]=(((cyc_h_rise*omega)/cyc_beta_rise)*(1-cos(2*pi*((cyc_tr[cr]-cyc_theta_rise_start)/cyc_beta_rise))))  #Velocity equation of the follower
   a_cyc_rise[cr]=((2*(((cyc_h_rise*pi)*(omega)**2)/(cyc_beta_rise))**2)*sin((2*pi*(cyc_tr[cr]-cyc_theta_rise_start)/cyc_beta_rise))) #Acceleration equation of the follower
  
  return (cyc_tr,s_cyc_rise,v_cyc_rise,a_cyc_rise) # return Theta,Displacement,Velocity,Acceleration
 
 elif cyc_theta_rise_start>=cyc_theta_rise_end: # If Initial angle Theta is greater than Final angle theta
     return "Initial cam_angle should be smaller than the final cam_angle." #return
 elif cyc_h_rise_start>=cyc_h_rise_end:          # If Initial displacement is higher than Final displacement
     return "Initial displacement must be smaller than the final displacement."  # return
