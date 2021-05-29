# Cam-Design
Constructs s-v-a diagram using various combinations of rise and fall functions and plots the cam profile.

## Features
There are nine different rise and fall follower functions available.
1. SHM Rise
2. SHM Fall
3. Cycloidal Rise
4. Cycloidal Fall
5. Parabolic/Uniform Acceleration and Retardation Rise
6. Parabolic/Uniform Acceleration and Retardation Fall
7. Linear/Constant Velocity rise
8. Linear/Constant Velocity rise
9. Dwell

The main file (cam_functions()) contains the program to take necessary user inputs and returns maximum values of Velocity and Acceleration. It also contains the sub-functions to plot s-v-a diagram and cam profile.
#### Note : max velocity and max acceleration are approximate values

#### There are lot of sophisticated expensive commercial softwares in the industry, which can design cams for modern engineering applications. However, for academic purposes it is not necessary because of the fact that students learn only basics of cam design. 

#### This project helps students and teachers to verify their design quickly with the drawing.  

## Usage
### Step 1
This project requires 'jupyter notebook' and the modules listed below.
1. Matplotlib 
2. numpy

How to install modules using pip : https://www.youtube.com/watch?v=bij66_Jtoqs

How to fix pip-'ModuleNotFoundError' : https://www.youtube.com/watch?v=cfFrYsGAVpo&t=105s

### Step 2
Make sure to paste all the files contained in the folder (Cam-files) to pwd (present working directory) of your jupyter notebook.

Note: 'Home Page' appeared after opening jupyter notebook is your present working directory.
https://usda-ars-gbru.github.io/ml-training-site/assets/images/jupyter-home.png

### Step 3 

Open Cam_file.ipynb from the home page and follow the instructions presented in the notebook.


## Output Visuals
For output visuals, please visit the folder "Output Visuals".

## Contributing
Contributions are always welcome. For better understanding read below.

#### 1. The file 'cam_functions.py' contains the code to take user inputs and also contains two other functions, that plots s-v-a diagram (sva_diagrams()) and cam profile ( cam_profile()).

#### 2. Other files have been named after their functions. To illustrate: shm_rise.py contains the function shm_rise() which returns the values of displacements, velocities and accelerations according to the simple harmonic rise equations.   

## Roadmap
#### Interested developers can create GUI for this project.

## Support
I'm available at mailtotransact@gmail.com

## References
Design of Machinery: An Introduction to the Synthesis and Analysis of Mechanisms and Machines (Mcgraw-Hill Series in Mechanical Engineering) by Robert L. Norton

Theory of Machines : SS Rattan

## License
[MIT](https://choosealicense.com/licenses/mit/)
