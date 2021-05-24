# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *
from matplotlib.pyplot import *
from cam_functions import *
from math import *
def cycloidal_fall(cyc_theta_fall_start,cyc_theta_fall_end,cyc_h_fall_start,cyc_h_fall_end,RPM): #Input- Start Angle, End Angle, Initial Displacement, Final Displacement, Cam shaft RPM
 if cyc_theta_fall_start<cyc_theta_fall_end and cyc_h_fall_start>cyc_h_fall_end:# Proceed if Start angle is smaller than End angle and Initial Displacement is higher than Final Displacement
  cyc_tf=linspace(cyc_theta_fall_start,cyc_theta_fall_end,endpoint=1) #Dividing the Cam Angle theta
  cyc_beta_fall=(cyc_theta_fall_end-cyc_theta_fall_start)  #Angle Beta
  cyc_h_fall=(cyc_h_fall_start-cyc_h_fall_end) #Displacement difference
  
  omega=degrees(2*pi*RPM/60) #Angular Velocity of Cam Shaft
  
  s_cyc_fall=empty(len(cyc_tf)) # Allocating empty array for Displacement of Cam Angle Theta
  v_cyc_fall=empty(len(cyc_tf)) # Allocating empty array for Velocity of Cam Angle Theta
  a_cyc_fall=empty(len(cyc_tf))  # Allocating empty array for Acceleration of Cam Angle Theta
  
  for cf in range(0,len(cyc_tf)):  # Looping the cam angles into equations
   s_cyc_fall[cf]=cyc_h_fall_start-((cyc_h_fall/pi)*(((pi*(cyc_tf[cf]-cyc_theta_fall_start)/(cyc_beta_fall))-((1/2)*sin(2*pi*((cyc_tf[cf]-cyc_theta_fall_start)/cyc_beta_fall))))))  #Displacement equation of the follower
   v_cyc_fall[cf]=-(((cyc_h_fall*omega)/cyc_beta_fall)*(1-cos(2*pi*((cyc_tf[cf]-cyc_theta_fall_start)/cyc_beta_fall))))   #Velocity equation of the follower
   a_cyc_fall[cf]=-((((2*((pi*cyc_h_fall)*(omega)**2)/(cyc_beta_fall))**2)*sin((2*pi*(cyc_tf[cf]-cyc_theta_fall_start)/cyc_beta_fall)))) #Acceleration equation of the follower
 
  return (cyc_tf,s_cyc_fall,v_cyc_fall,a_cyc_fall) # return Theta,Displacement,Velocity,Acceleration
 
 elif cyc_theta_fall_start>=cyc_theta_fall_end: # If Initial Theta Angle is greater than Final Theta Angle
     return "Initial cam_angle should be smaller than the final cam_angle." #return
 elif cyc_h_fall_start<=cyc_h_fall_end:         # If Initial displacement is smaller than Final displacement
     return "Initial displacement must be higher than the final displacement." # return