import RPi.GPIO as GPIO
from time import sleep
import time
import rospy
import sys
import os
import math

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(18,GPIO.OUT)
	GPIO.setup(7,GPIO.OUT)
	GPIO.setup(19,GPIO.OUT)
	GPIO.setup(3,GPIO.OUT)
	GPIO.setup(24,GPIO.OUT)
	GPIO.setup(26,GPIO.OUT)

def forward():
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(18,GPIO.LOW)

def stop():
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)

def backward():
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.HIGH)

def left():
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.HIGH)

def right():
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(18,GPIO.LOW)

def servo_up():

	GPIO.output(7,GPIO.LOW)
	GPIO.output(19,GPIO.LOW)
	GPIO.output(3,GPIO.LOW)
def servo_down():

	GPIO.output(7,GPIO.HIGH)
	GPIO.output(19,GPIO.HIGH)
	GPIO.output(3,GPIO.HIGH)

def screw_in():
	GPIO.output(24,GPIO.LOW)
	GPIO.output(26,GPIO.HIGH)

def screw_out():
	GPIO.output(24,GPIO.HIGH)
	GPIO.output(26,GPIO.LOW)


def callback(self,event=None):
	if(rospy.get_param('/parameter/combo') == True):
#		print "true"
		if(rospy.get_param('/parameter/button/frwdbutton') == True):
			forward()
		elif(rospy.get_param('/parameter/button/backbutton') == True):
			backward()
		elif(rospy.get_param('/parameter/button/leftbutton')== True):
			left()
		elif(rospy.get_param('/parameter/button/rightbutton')==True):
			right()
		elif(rospy.get_param('/parameter/button/servo_up')==True):
			servo_up()
			print "servo up"
		#elif(rospy.get_param('/parameter/button/servo_down')==True):
		#	servo_down()
		#	print "servo down"
		elif(rospy.get_param('/parameter/button/screw_in') == True):
			screw_in()
			print "screw in"
		elif(rospy.get_param('/parameter/button/screw_out')==True):
			screw_out()
			print "screw out"
		else:
			stop()
			servo_down()
			print "servo down"
	elif(rospy.get_param('/parameter/indiv')== True):
		if(rospy.get_param('/parameter/robot1')==True):
			print "robot 1 true"
			if(rospy.get_param('/parameter/button/frwdbutton') == True):
				forward()	
			elif(rospy.get_param('/parameter/button/backbutton') == True):
				backward()
			elif(rospy.get_param('/parameter/button/leftbutton') == True):
				left()
			elif(rospy.get_param('/parameter/button/rightbutton') == True):
				right()
			elif(rospy.get_param('/parameter/button/servo_up') == True):
				servo_up()
			elif(rospy.get_param('/parameter/button/screw_in') == True):
				screw_in()
			elif(rospy.get_param('/parameter/button/screw_out') == True):
				screw_out()
			else:
				stop()
				servo_down()
		else:
			print "robot1 false"
			stop()

	else:
		stop()
		servo_down()



if __name__ == "__main__":
	try:
		init()
		rospy.init_node('visual_servo',anonymous=True)
		rospy.Timer(rospy.Duration(0.01),callback)
		rospy.spin()
	except:
		GPIO.cleanup()
