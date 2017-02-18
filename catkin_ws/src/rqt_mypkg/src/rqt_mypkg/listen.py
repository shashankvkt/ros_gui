import rospy
import os
import sys
import rospkg


if rospy.get_param('/parameter/button/playbutton') == True:
	print "true"
else:
	print "false"