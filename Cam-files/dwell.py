# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *
def dwell(dwell_theta_start,dwell_theta_end,h_dwell): # input- Start angle, End Angle, Displacement
   if dwell_theta_start<dwell_theta_end and h_dwell >=0: # Proceed if-Start angle is smaller than End angle and Displacement is greater than zero
    td=linspace(dwell_theta_start,dwell_theta_end) # Dividing the Cam angle theta 
    ld=len(td) # Length of the array 'td'
   
    s_dwell=(h_dwell+zeros(ld)) #Displacement of the follower
    v_dwell=0*s_dwell           #Velocity of the follower
    a_dwell=0*v_dwell           #Acceleration of the follower
    
    return (td,s_dwell,v_dwell,a_dwell) # return Theta,Displacement,Velocity,Acceleration
   
   elif dwell_theta_start>=dwell_theta_end: # if initial angle theta is greater than final angle theta
       return "Initial cam_angle should be smaller than the final cam_angle." # return
   elif h_dwell<0:                          # if displacement is lesser than zero 
       return"Invalid input,displacement must be greater or equal to zero." # return