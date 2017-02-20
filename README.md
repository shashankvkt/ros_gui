# ros_gui
This repository is a ROS based Graphic User Interface to control a multi-agent robotic system. The project has been developed with reference to the idea of Detachable Modular Robot capable of Cooperative Climbing and Multi Agent Exploration which can be refered from the following link  

   http://robotics.iiit.ac.in/people/harsha.turlapati/DCMR/icra17.html  
   
In this project we used RaspberryPi 3 model, on 4 different robots each identified by a different namespace. The RPis (Client) and the laptop (Server) were connected on a common wireless network.  
    
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

8.Since the project involves a multi agent robot system, it becomes essential to be able to control the robots individually as well as control all of them at once.  
It majorly involves the use of 2 checkboxes, namely  
a.command all  robots  
b.command indiv robots  

9.When the "Command all robots" check box is selected as depicted in the picture below, the directional commands of forward, backward, ;eft, right, servo and screwing controls are given to all the robots simultaneously.  

![screenshot from 2017-02-19 13_27_07](https://cloud.githubusercontent.com/assets/23419376/23101224/a529eee0-f6b4-11e6-85e9-ebeea2705033.png)  

10.Individual robots can be controlled by selecting the "command individual robots" checkbo and then selecting the robot number on which the directional commands are expected to execute. The following is an example of using the checkbox.  

![screenshot from 2017-02-19 13_46_39](https://cloud.githubusercontent.com/assets/23419376/23101244/00364e32-f6b5-11e6-98fd-e8c7ac85339b.png)  

11.When a particular check box is selected or when a particular command is given from the GUI (say forward), the corresponding command is given in the form of a ROS parameter. The value of the ROS parameter determines TRUE/FALSE value of that particular motion which can be changed in the "my_widget.py" file.  

12.For the robot to execute a command selected from the GUI, follow the following steps:  

a.When you start roscore on the server side, Copy the following command in your client (Rpi) directory:

    ROS_MASTER_URI=http://< >
b.Copy the following file into your client (Rpi) directory:

    motor_move.py
c.To execute the code, execute the following command:

    python motor_move.py
d.Now press the different icons on the GUI, to see it's respective motion being executed by the robot.
