# ros_gui
This repository is a ROS based Graphic User Interface to control a multi-agent robotic system. The project has been developed with reference to the idea of Detachable Modular Robot capable of Cooperative Climbing and Multi Agent Exploration which can be refered fron the following link  

   http://robotics.iiit.ac.in/people/harsha.turlapati/DCMR/icra17.html  
  
    
The following are the steps in order to install and execute this package  
1. Install ROS-indigo 
2.Create a catkin workspace  
3. In the src folder type the following command  

    git clone https://github.com/shashankvkt/ros_gui.git 
 
 4.compile your paackage by typing the following command in your catkin_ws directory.

    catkin_make  
    
5.Open a new terminal and type

    roscore
    
6.Open another terminal and type the following command

    rqt --standalone rqt_mypkg
7.The following picture appears on the screen showing the GUI  

![screenshot from 2017-02-19 13 20 03](https://cloud.githubusercontent.com/assets/23419376/23100485/1c63bb9c-f6a8-11e6-9446-1bb907244dfe.png)  

Since the project involves a multi agent robot system, it becomes essential to be able to control the robots individually as well as control all of them at once.  
It majorly involves the use of 2 checkboxes, namely  
a.command all  robots  
b.command indiv robots

