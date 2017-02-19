# ros_gui
This repository is a ROS based Graphic User Interface to control a multi-agent robotic system. The project has been developed with refernce to the idea of Detatchable Compliant Modular Robotic system which can be refered fron the following link  

   http://robotics.iiit.ac.in/people/harsha.turlapati/DCMR/icra17.html  
  
    
The following are the steps in order to install and execute this package  
1. Install ROS-indigo 
2.Create a catkin workspace  
3. In the src folder type the following command  

    git clone https://github.com/shashankvkt/ros_gui.git  
    
4.compile your paackage by typing the following command in your catkin_Ws directory.

    catkin_make
5. Open a new terminal and type 
    roscore
6. Open another terminal and type the following command 
    rqt --standalone rqt_mypkg
