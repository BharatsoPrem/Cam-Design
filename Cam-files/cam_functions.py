# -*- coding: utf-8 -*-
"""
@author: Bharat P
"""
from numpy import *                                    # Import all the necessary modules
from math import *
from matplotlib.pyplot import *
from shm_rise import *
from shm_fall import *
from cycloidal_rise import *
from cycloidal_fall import *
from dwell import *
from linear_rise import *
from linear_fall import *
from uar_rise import *
from uar_fall import *
def cam_functions():
    print('List  of available Cam  functions\n')       # Listing down the cam functions
    print('1.Simple Harmonic rise\n')
    print('2.Simple Harmonic fall\n')
    print('3.Cycloidal rise\n')
    print('4.Cycloidal fall\n')
    print('5.Parabolic/Uniform Acceleration and Retardation rise\n')
    print('6.Parabolic/Uniform Acceleration and Retardation fall\n')
    print('7.Linear rise\n')
    print('8.Linear fall\n')
    print('9.Dwell\n')
    x=[];s=[];v=[];a=[];lz=[];las=[]   # Creating empty lists to store displacements, velocities, accelerations and operation counts
    global X,S,base_circ,V,A,RPM   # Declaring displacements, velocities, base circle radius and cam angles as global variables
    RPM=float(input('Enter Cam-Shaft RPM\n')) # input Cam shaft RPM
    if RPM<=0:
         return 'Enter a Valid Input'
    fundic={1:'Simple Harmonic rise',2:'Simple Harmonic fall',3:'Cycloidal rise',4:'Cycloidal fall',5:'Parabolic rise',6:'Parabolic fall',7:'Linear rise',8:'Linear fall',9:'Dwell'}
    # The above dictionary is to map index to type of cam function
    try:
     base_circ=float(input('Enter the radius of base circle in mm\n')) # input base circle radius of Cam
     if base_circ<=0:
         return 'Base circle radius should be positive'
    except ValueError or NameError:
        return 'Enter a valid input'
    p=0 # initializing index to 0
    print('Warning:Maintain the order of inputs for angles & displacement values and seperate the values by commas only')
    while p!=-1: # Keep taking inputs until index gets -1
     try:
         p=int(input('Enter corresponding index of the function to select that particular function or press -1 to exit\n'))# input index 
         if p!=-1 and p>0 and p<=9:
          lz.append(p) # append the index to list lz
         else:
             continue  # if "if" condition is not satisfied go back to input index again
     except ValueError:
         return 'Enter valid inputs'
     if p==1:
        try:
            global x1,s1,v1,a1  # declaring the inputs of shm rise function as global 
            (i1,j1,k1,l1)=(input('''SHM _Rise selected: Enter in order
                             \n('Start angle, Final angle, Initial displacement, Final displacement')\n''').split(','))
        except ValueError:
            return 'Enter valid inputs'
        try:
         [x1,s1,v1,a1]=shm_rise(float(i1),float(j1),float(k1),float(l1),RPM) # calling the shm_rise function and passing inputs
         x.append(x1);v.append(v1) # append cam angles,displacement,velocity and acceleration of shm rise function to lists 'x' 's' 'v' 'a' respectively 
         s.append(s1);a.append(a1) 
         print('success!')
        except ValueError:# If expected 4 outputs is not returned then display the error stated by shm_rise function
            er1=shm_rise(float(i1),float(j1),float(k1),float(l1),RPM) 
            print(er1,': Try again!')
            continue
     if p==2: # same procedure followed here as it was followed in p==1 loop
        try: 
            global x2,s2,v2,a2
            (i2,j2,k2,l2)=(input('''SHM _Fall selected: Enter in order 
                              \n('Start angle, Final angle, Initial displacement, Final displacement')\n''').split(','))
        except ValueError:
            return 'Enter valid inputs'
        try:
           [x2,s2,v2,a2]=shm_fall(float(i2),float(j2),float(k2),float(l2),RPM)
           x.append(x2);v.append(v2)
           s.append(s2);a.append(a2)
           print('success!')
        except ValueError:
            er2=shm_fall(float(i2),float(j2),float(k2),float(l2),RPM)
            print(er2,': Try again!')
            continue
     if p==3: # same procedure followed here as it was followed in p==1 loop
         try:
            global x3,s3,v3,a3
            (i3,j3,k3,l3)=(input('''Cycloidal rise selected: Enter in order 
                              \n('Start angle, Final angle, Initial displacement, Final displacement')\n''').split(','))
         except ValueError:
             return 'Enter valid inputs'
         try:
           [x3,s3,v3,a3]=cycloidal_rise(float(i3),float(j3),float(k3),float(l3),RPM)
           x.append(x3);v.append(v3)
           s.append(s3);a.append(a3)
           print('success!')
         except ValueError:
            er3=cycloidal_rise(float(i3),float(j3),float(k3),float(l3),RPM)
            print(er3,': Try again!')
            continue
     
     if p==4: # same procedure followed here as it was followed in p==1 loop
        try:
            global x4,s4,v4,a4
            (i4,j4,k4,l4)=(input('''Cycloidal fall selected: Enter in order
                         \n('Start angle, Final angle, Initial displacement, Final displacement)'\n''').split(','))
        except ValueError:
            return 'Enter valid inputs'
        try:
           [x4,s4,v4,a4]=cycloidal_fall(float(i4),float(j4),float(k4),float(l4),RPM)
           x.append(x4);v.append(v4)
           s.append(s4);a.append(a4)
           print('success!')
        except ValueError:
            er4=cycloidal_fall(float(i4),float(j4),float(k4),float(l4),RPM)
            print(er4,': Try again!')
            continue
    
     if p==5: # same procedure followed here as it was followed in p==1 loop
        try:
         global x5,s5,v5,a5
         (i5,j5,k5,l5)=(input('''Parabolic rise selected: Enter in order
                          \n('Start angle,  Final angle, Initial displacement, Final displacement')\n''').split(','))
        except ValueError:
            return 'Enter valid inputs'
        try:
           [x5,s5,v5,a5]=uar_rise(float(i5),float(j5),float(k5),float(l5),RPM)
           x.append(x5);v.append(v5)
           s.append(s5);a.append(a5)
           print('success!')
        except ValueError:
            er5=uar_rise(float(i5),float(j5),float(k5),float(l5),RPM)
            print(er5,': Try again!')
            continue
     if p==6: # same procedure followed here as it was followed in p==1 loop
         try:
            global x6,s6,v6,a6
            (i6,j6,k6,l6)=(input('''Parabolic fall selected: Enter in order
                          \n('Start angle, Final angle, Initial displacement, Final displacement')\n''').split(','))
         except ValueError:
             return 'Enter valid inputs'
         try:
           [x6,s6,v6,a6]=uar_fall(float(i6),float(j6),float(k6),float(l6),RPM)
           x.append(x6);v.append(v6)
           s.append(s6);a.append(a6)
           print('success!')
         except ValueError:
            er6=uar_rise(float(i6),float(j6),float(k6),float(l6),RPM)
            print(er6,': Try again!')
            continue
     if p==7: # same procedure followed here as it was followed in p==1 loop
         try:
            global x7,s7,v7,a7
            (i7,j7,k7,l7)=(input('''Linear rise selected: Enter in order
                          \n('Start angle, Final angle, Initial displacement, Final displacement)'\n''').split(','))
         except ValueError:
             return 'Enter valid inputs'
         try:
           [x7,s7,v7,a7]=linear_rise(float(i7),float(j7),float(k7),float(l7),RPM)
           x.append(x7);v.append(v7)
           s.append(s7);a.append(a7)
           print('success!')
         except ValueError:
            er7=linear_rise(float(i7),float(j7),float(k7),float(l7),RPM)
            print(er7,': Try again!')
            continue
     if p==8: # same procedure followed here as it was followed in p==1 loop
        try:
            global x8,s8,v8,a8
            (i8,j8,k8,l8)=(input('''Linear fall selected: Enter in order
                          \n('Start angle, Final angle, Initial displacement, Final displacement')\n''').split(','))
        except ValueError:
            return 'Enter valid inputs'
        try:
           [x8,s8,v8,a8]=linear_fall(float(i8),float(j8),float(k8),float(l8),RPM)
           x.append(x8);v.append(v8)
           s.append(s8);a.append(a8)
           print('success!')
        except ValueError:
            er8=linear_fall(float(i8),float(j8),float(k8),float(l8),RPM)
            print(er8,': Try again!')
            continue
     if p==9:# same procedure followed here as it was followed in p==1 loop except that RPM is not necessary
         try:
            global x9,s9,v9,a9
            (i9,j9,k9)=(input('''Dwell selected: Enter in order
                         \n('Start angle, Final angle, Current displacement')\n''').split(','))
         except ValueError:
             return 'Enter valid inputs'
         try:
           [x9,s9,v9,a9]=dwell(float(i9),float(j9),float(k9))
           x.append(x9);v.append(v9)
           s.append(s9);a.append(a9)
           print('success!')
         except ValueError:
            er9=cycloidal_rise(float(i9),float(j9),float(k9))
            print(er9,': Try again!')
            continue
    try:
     X=concatenate(x) # Concatenate all the Cam angle values
     S=concatenate(s) # Concatenate all the Displacement values
     V=concatenate(v) # Concatenate all the Velocity values
     A=concatenate(a) # Concatenate all the Acceleration values
     for kk in lz:    # From the list of appended indicies, pass the indicies as key values to display all the functions selected  
         las.append(fundic[kk])
     print("Functions selected : ",las)
     return print('Max velocity=', max(V),'mm/s','\nMax Acceleration=', max(A),'mm/s^2') # retrun maximum values of Displacement, Velocity and Acceleration
     
    except ValueError or NameError:
         return    

from cam_functions import *      
def sva_diagrams():
     figure()                    
     style.use('dark_background') # Set the background to black
     figure(figsize=(7,6),dpi=350) # Set the resolution of the figure
     tight_layout()                # Fit the plot cleanly
     subplot(3,1,1)                # Three plots are needed in order of 3 rows and 1 column order, this being first among them
     plot(X,S)                     # Plot Cam angles vs Displacement  values
     xlabel('Cam Angle (deg)')     # Label x-axis
     ylabel('Follower\nDisplacement')# Label y-axis
     xticks(linspace(0,360,10))     # Set the markings of x-axis
     xlim(0,360)                    # Limit the x-axis from 0 to 360
     grid(True)                    # Include grid
     title('s-v-a diagrams')       # Add title to the plot
     
     subplot(3,1,2)                # Second plot among three plots
     plot(X,V,color='red')         # Plot Cam angles vs Velocity values
     xlabel('Cam Angle')           # Label x-axis
     ylabel('Follower\nVelocity')  # Label y-axis
     xticks(linspace(0,360,10))    # Set the markings on x-axis
     xlim(0,360)                   # Limit the x-axis from 0 to 360
     grid(True)                    # Include grid
     
     subplot(3,1,3)                #Third plot among three plots
     plot(X,A,color='magenta')     #Plot Cam angles vs Acceleration values
     xlabel('Cam Angle')           # Label x-axis
     ylabel('Follower\nAcceleration') # Label y-axis
     xticks(linspace(0,360,10))    # Set the markings on x-axis
     xlim(0,360)                   # Limit the x-axis from 0 to 360
     grid(True)                    # Include grid

from cam_functions import *   
def cam_profile():
    print('List of Cam Profiles\n')                   #Listing the cam profiles
    print('1.Knife Edge\n')
    print('2.Roller Follower\n')
    print('3.Flat face/Mushroom follower\n')
    
    c=int(input('Enter corresponding index of the Cam Profile to select that particular Profile\n')) #input the index 
   
    # knife edge
    if c==1:
     e_ke=float(input('offset length in mm\n'))  # Offset value
     rot_ke=int(input('Direction of rotation : Enter 1 for clockwise / -1 for anticlockwise\n')) # Specify the direction of rotation
     if rot_ke==1 or rot_ke==-1:
       pol_ke=empty(len(X))  # Allocating space for radial distance for polar plot
       thet_ke=empty(len(X)) # Allocating space for angle theta for polar plot 
       So_ke=sqrt((base_circ)**2-(e_ke**2)) # Distance between offset circle and base circle
       for ke in range(0,len(X)):
          xi=(cos(rot_ke*X[ke]*pi/180)*(So_ke+S[ke])-(e_ke*sin(rot_ke*X[ke]*pi/180))) # Equation of x co-ordinates of knife edge cam profile
          yi=(sin(rot_ke*X[ke]*pi/180)*(So_ke+S[ke])+(e_ke*cos(rot_ke*X[ke]*pi/180))) # Equation of y co-ordinates of knife edge cam profile
          pol_ke[ke]=sqrt((xi**2+yi**2))    # Transforming x-y co-ordinates to 'radial distance-r' in polar plot
          if xi>0:
           thet_ke[ke]=atan(yi/xi)          # Trnsforming x-y co-ordinates to 'angle theta' in polar plot
          else:
              thet_ke[ke]=(atan((yi/xi))+pi)
       
       figure(figsize=(7,5),dpi=400,facecolor='#000000') # Set the resolution of the figure and set the background black(rgb)
       style.use('dark_background')                     # Set the plot background as black
       subplot(111,projection='polar')                  # setting the projection to polar
       plot(thet_ke,base_circ*ones(len(X)),'g',linewidth='2',label='Base Circle') # Plotting theta vs base circle
       plot(thet_ke,e_ke*ones(len(X)),'b',linewidth='2',label='Offset Circle') # Plotting offset circle
       plot(thet_ke,pol_ke,'r',linewidth='2',label='Cam Profile')   # Plotting cam profile
       axis(True)                                       # Set the axis 
       legend(bbox_to_anchor=(0,1),loc=(0,1))           # Locate the legend at the top left corner 
       tight_layout()                                   # Fit the plot cleanly
       fill_between(thet_ke,pol_ke,color='orange')      # Fill the cam profile with the given colour
     else:
        return 'Only +1 and -1 are allowed'    
    
    #Roller Follower
    if c==2:
        e_rol=float(input('offset length in mm\n')) # Offset value
        Rf=float(input('Radius of follower in mm\n')) # Radius of roller circle
        rot_rol=int(input('Direction of rotation : Enter 1 for clockwise / -1 for anticlockwise\n')) # Specify the direction of rotation
        if rot_rol==1 or rot_rol==-1: 
         thet_rol=empty(len(X)) # Allocating space for radial distance for polar plot
         pol_rol=empty(len(X))  # Allocating space for angle theta for polar plot
          
         for rol in range(0,len(X)):
              xr=((base_circ+S[rol])*cos(radians(rot_rol*X[rol])))-e_rol*sin(radians(rot_rol*X[rol])) # Equation of x co-ordinates of roller follower cam profile
              yr=((base_circ+S[rol])*sin(radians(rot_rol*X[rol])))+e_rol*cos(radians(rot_rol*X[rol])) # Equation of y co-ordinates of roller follower cam profile
              pol_rol[rol]=sqrt((xr**2)+(yr**2)) # Transforming x-y co-ordinates to 'radial distance-r' in polar plot
              if xr>0:
               thet_rol[rol]=(atan(yr/xr)) # Transforming x-y co-ordinates to 'angle theta' in polar plot
              else:
                  thet_rol[rol]=(atan(yr/xr)+pi)
         figure(figsize=(7,5),dpi=400,facecolor='#000000') # Set the resolution of the figure and set the background black(rgb)
         style.use('dark_background')                      # Setting the plot background to black
         subplot(111,projection='polar')                   # setting the projection to polar
         plot(thet_rol,(base_circ+Rf)*ones(len(X)),'g',linewidth='2',label='Prime Circle')
         plot(thet_rol,base_circ*ones(len(X)),'m',linewidth='2',label='Base Circle')
         plot(thet_rol,e_rol*ones(len(X)),'b',linewidth='2',label='Offset Circle')
         plot(thet_rol,pol_rol,'r',linewidth='2',label='Cam Profile')
         axis(True)                                       # Set the axis 
         legend(bbox_to_anchor=(0,1),loc=(0,1))           # Locate the legend at the top left corner 
         tight_layout()                                   # Fit the plot cleanly
         fill_between(thet_rol,pol_rol,color='orange')    # Fill the cam profile with the given colour
        else:
            return 'Only +1 and -1 are allowed'
   
    #mushroom follower
    if c==3:
       rot_mush=int(input('Direction of rotation : Enter 1 for clockwise / -1 for anticlockwise\n')) # Specify the direction of rotation
       if rot_mush==1 or rot_mush==-1: 
        omega=degrees(2*pi*RPM/60) # Angular velocity
        thet_mush=empty(len(X)) # Allocating space for radial distance for polar plot
        pol_mush=empty(len(X))  # Allocating space for angle theta for polar plot
        
        for mush in range(0,len(X)):
            
            alpha_mush=atan((V[mush]/omega)*(1/(base_circ+S[mush]))) 
            xm=(((base_circ+S[mush])/(cos(alpha_mush)))*cos(rot_mush*radians(X[mush])+alpha_mush)) # Equation of x co-ordinates of mushroom follower cam profile
            ym=(((base_circ+S[mush])/(cos(alpha_mush)))*sin(rot_mush*radians(X[mush])+alpha_mush)) # Equation of y co-ordinates of mushroom follower cam profile
            
            pol_mush[mush]=sqrt((xm**2)+(ym**2)) # Transforming x-y co-ordinates to 'radial distance-r' in polar plot
            if xm>0:
               thet_mush[mush]=(atan(ym/xm))     # Transforming x-y co-ordinates to 'angle theta' in polar plot
            else:
                  thet_mush[mush]=(atan(ym/xm)+pi)
        figure(figsize=(7,5),dpi=400,facecolor='#000000') # Set the resolution of the figure and set the background black(rgb)
        style.use('dark_background')                      # Setting the plot background to black
        subplot(111,projection='polar')                   # setting the projection to polar
        plot(thet_mush,base_circ*ones(len(X)),'m',linewidth='2',label='Base Circle')
        plot(thet_mush,pol_mush,'r',linewidth='2',label='Cam Profile')
        axis(True)                                       # Set the axis 
        legend(bbox_to_anchor=(0,1),loc=(0,1))           # Locate the legend at the top left corner 
        tight_layout()                                   # Fit the plot cleanly
        fill_between(thet_mush,pol_mush,color='orange')  # Fill the cam profile with the given colour
       else:
           return 'Only +1 and -1 are allowed'